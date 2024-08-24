from flask import Flask, render_template, redirect, url_for, request, jsonify, session, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, set_access_cookies, unset_jwt_cookies, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_cors import CORS
from functools import wraps
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # For simplicity, you might want to enable this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # Adjust as needed.

cors = CORS(app)

db.init_app(app)

jwt = JWTManager(app)

def jwt_required_with_optional_redirect(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except:
            return redirect(url_for('login'))
        return view_function(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return render_template('signup.html', error='Email already exists.')

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.form
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.username)
        resp = make_response(redirect(url_for('dashboard')))
        set_access_cookies(resp, access_token)
        return resp
    else:
        return render_template('login.html', error='Invalid email or password.')

@app.route('/current_user', methods=['GET'])
@jwt_required()
def current_user_info():
    identity = get_jwt_identity()
    print(f"Identity received: {identity}")
    return jsonify({'username': identity['username']})

@app.route('/dashboard')
@jwt_required_with_optional_redirect
def dashboard():
    current_user = get_jwt_identity()
    return render_template('dashboard.html', username=current_user)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    resp = make_response(redirect(url_for('login')))
    unset_jwt_cookies(resp)
    return resp

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return redirect(url_for('login'))

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)