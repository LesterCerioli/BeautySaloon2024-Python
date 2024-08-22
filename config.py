# Configuration settings for PostgreSQL
import os


SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/beauty_salon_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')