import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///appointments.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'