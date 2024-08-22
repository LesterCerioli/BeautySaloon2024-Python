from sqlalchemy.exc import SQLAlchemyError
from application import db  # Import the db instance from your application module
from application.viewmodels.attendantviewmodel import Attendant

class AttendantController:
    
    @staticmethod
    def create_attendant(data):
        try:
            # Create a new Attendant object
            attendant = Attendant(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number']
            )
            # Add and commit to the database
            db.session.add(attendant)
            db.session.commit()
            return attendant
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
    
    @staticmethod
    def get_attendant(attendant_id):
        try:
            # Fetch the Attendant by ID
            attendant = Attendant.query.get(attendant_id)
            if not attendant:
                raise ValueError("Attendant not found")
            return attendant
        except ValueError as e:
            raise ValueError(str(e))
    
    @staticmethod
    def update_attendant(attendant_id, data):
        try:
            # Fetch the Attendant by ID
            attendant = Attendant.query.get(attendant_id)
            if not attendant:
                raise ValueError("Attendant not found")

            # Update the Attendant's details
            if 'name' in data:
                attendant.name = data['name']
            if 'email' in data:
                attendant.email = data['email']
            if 'phone_number' in data:
                attendant.phone_number = data['phone_number']
            
            # Commit the changes
            db.session.commit()
            return attendant
        except ValueError as e:
            raise ValueError(str(e))
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
    
    @staticmethod
    def delete_attendant(attendant_id):
        try:
            # Fetch the Attendant by ID
            attendant = Attendant.query.get(attendant_id)
            if not attendant:
                raise ValueError("Attendant not found")

            # Delete the Attendant
            db.session.delete(attendant)
            db.session.commit()
        except ValueError as e:
            raise ValueError(str(e))
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
