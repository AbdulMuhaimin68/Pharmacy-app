import os

DB_NAME = os.getenv("DB_NAME")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
DB_PORT = os.getenv("DB_PORT")
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key'