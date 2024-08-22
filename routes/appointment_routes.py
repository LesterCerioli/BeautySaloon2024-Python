from flask import Blueprint, request, jsonify
from flasgger import swag_from

from rest.controllers.appointmentcontroller import AppointmentController


appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/create', methods=['POST'])
@swag_from({
    'tags': ['Appointments'],
    'description': 'Create a new appointment',
    'parameters': [
        {
            'name': 'appointment',
            'description': 'Appointment object',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'date': {'type': 'string', 'example': '2024-08-21T00:00:00Z'},
                    'appointment_hour': {'type': 'string', 'example': '2024-08-21T15:00:00Z'}
                },
                'required': ['date', 'appointment_hour']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Appointment created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Appointment created successfully'},
                    'appointment': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'date': {'type': 'string'},
                            'appointment_hour': {'type': 'string'}
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Bad request',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def create_appointment():
    try:
        data = request.get_json()
        appointment = AppointmentController.create_appointment(data)
        return jsonify({
            "message": "Appointment created successfully",
            "appointment": {
                "id": str(appointment.id),
                "date": appointment.date.isoformat(),
                "appointment_hour": appointment.appointment_hour.isoformat()
            }
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@appointment_bp.route('/<uuid:appointment_id>', methods=['GET'])
@swag_from({
    'tags': ['Appointments'],
    'description': 'Get appointment by ID',
    'parameters': [
        {
            'name': 'appointment_id',
            'description': 'Appointment ID',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Appointment details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'date': {'type': 'string'},
                    'appointment_hour': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Appointment not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def get_appointment(appointment_id):
    try:
        appointment = AppointmentController.get_appointment(appointment_id)
        return jsonify({
            "id": str(appointment.id),
            "date": appointment.date.isoformat(),
            "appointment_hour": appointment.appointment_hour.isoformat()
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@appointment_bp.route('/<uuid:appointment_id>', methods=['PUT'])
@swag_from({
    'tags': ['Appointments'],
    'description': 'Update an appointment by ID',
    'parameters': [
        {
            'name': 'appointment_id',
            'description': 'Appointment ID',
            'in': 'path',
            'type': 'string',
            'required': True
        },
        {
            'name': 'appointment',
            'description': 'Updated appointment details',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'date': {'type': 'string'},
                    'appointment_hour': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Appointment updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'appointment': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'date': {'type': 'string'},
                            'appointment_hour': {'type': 'string'}
                        }
                    }
                }
            }
        },
        '404': {
            'description': 'Appointment not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def update_appointment(appointment_id):
    try:
        data = request.get_json()
        appointment = AppointmentController.update_appointment(appointment_id, data)
        return jsonify({
            "message": "Appointment updated successfully",
            "appointment": {
                "id": str(appointment.id),
                "date": appointment.date.isoformat(),
                "appointment_hour": appointment.appointment_hour.isoformat()
            }
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@appointment_bp.route('/<uuid:appointment_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Appointments'],
    'description': 'Delete an appointment by ID',
    'parameters': [
        {
            'name': 'appointment_id',
            'description': 'Appointment ID',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Appointment deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Appointment deleted successfully'}
                }
            }
        },
        '404': {
            'description': 'Appointment not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def delete_appointment(appointment_id):
    try:
        AppointmentController.delete_appointment(appointment_id)
        return jsonify({"message": "Appointment deleted successfully"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500