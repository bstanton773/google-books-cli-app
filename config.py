import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__name__), '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.environ.get('SQLALCHEMY_DATABASE_URI').startswith('postgres'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')