

class DatabaseConfig:
    @staticmethod
    def set_session_options(app):
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @staticmethod
    def initialize_database(app, db):
        db.init_app(app)
        with app.app_context():
            db.create_all()