from typing import Optional
from dataclasses import dataclass, field

app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Initialize the database
db.init_app(app)

# Register blueprints (routes)
app.register_blueprint(salon_bp, url_prefix='/salon')
app.register_blueprint(customer_bp, url_prefix='/customer')
app.register_blueprint(appointment_bp, url_prefix='/appointment')
app.register_blueprint(attendant_bp, url_prefix='/attendant')
app.register_blueprint(location_bp, url_prefix='/location')

if __name__ == '__main__':
    app.run(debug=True)
