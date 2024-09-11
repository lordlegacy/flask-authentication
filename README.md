# Flask JWT Authentication App

This is a simple Flask application that demonstrates user authentication using JWT (JSON Web Tokens). The app allows users to sign up, log in, and access a protected dashboard.

## Features

- User registration (sign up)
- User authentication (log in)
- JWT-based session management
- Protected routes
- User logout
- SQLAlchemy for database management

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)
- A SQL database (e.g., SQLite, PostgreSQL)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-jwt-auth-app.git
   cd flask-jwt-auth-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

## Usage

1. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main application file containing routes and JWT configuration
- `models.py`: Database models
- `templates/`: HTML templates for the application
- `static/`: Static files (CSS, JavaScript, etc.)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

## Contact

If you have any questions, please open an issue or contact [your-email@example.com](mailto:your-email@example.com).
