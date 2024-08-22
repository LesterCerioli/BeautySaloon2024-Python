from flask import Blueprint, request, jsonify

from flasgger import swag_from

from rest.controllers.attendantcontroller import AttendantController

attendant_bp = Blueprint('attendant', __name__)

@attendant_bp.route('/create', methods=['POST'])
@swag_from({
    'tags': ['Attendants'],
    'description': 'Create a new attendant',
    'parameters': [
        {
            'name': 'attendant',
            'description': 'Attendant object',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'John Doe'},
                    'email': {'type': 'string', 'example': 'john.doe@example.com'},
                    'phone_number': {'type': 'string', 'example': '+1234567890'}
                },
                'required': ['name', 'email', 'phone_number']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Attendant created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Attendant created successfully'},
                    'attendant': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'email': {'type': 'string'},
                            'phone_number': {'type': 'string'}
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
def create_attendant():
    try:
        data = request.get_json()
        attendant = AttendantController.create_attendant(data)
        return jsonify({
            "message": "Attendant created successfully",
            "attendant": {
                "id": str(attendant.id),
                "name": attendant.name,
                "email": attendant.email,
                "phone_number": attendant.phone_number
            }
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@attendant_bp.route('/<uuid:attendant_id>', methods=['GET'])
@swag_from({
    'tags': ['Attendants'],
    'description': 'Get attendant by ID',
    'parameters': [
        {
            'name': 'attendant_id',
            'description': 'Attendant ID',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Attendant details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone_number': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Attendant not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def get_attendant(attendant_id):
    try:
        attendant = AttendantController.get_attendant(attendant_id)
        return jsonify({
            "id": str(attendant.id),
            "name": attendant.name,
            "email": attendant.email,
            "phone_number": attendant.phone_number
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@attendant_bp.route('/<uuid:attendant_id>', methods=['PUT'])
@swag_from({
    'tags': ['Attendants'],
    'description': 'Update an attendant by ID',
    'parameters': [
        {
            'name': 'attendant_id',
            'description': 'Attendant ID',
            'in': 'path',
            'type': 'string',
            'required': True
        },
        {
            'name': 'attendant',
            'description': 'Updated attendant details',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone_number': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Attendant updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'attendant': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'name': {'type': 'string'},
                            'email': {'type': 'string'},
                            'phone_number': {'type': 'string'}
                        }
                    }
                }
            }
        },
        '404': {
            'description': 'Attendant not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def update_attendant(attendant_id):
    try:
        data = request.get_json()
        attendant = AttendantController.update_attendant(attendant_id, data)
        return jsonify({
            "message": "Attendant updated successfully",
            "attendant": {
                "id": str(attendant.id),
                "name": attendant.name,
                "email": attendant.email,
                "phone_number": attendant.phone_number
            }
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@attendant_bp.route('/<uuid:attendant_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Attendants'],
    'description': 'Delete an attendant by ID',
    'parameters': [
        {
            'name': 'attendant_id',
            'description': 'Attendant ID',
            'in': 'path',
            'type': 'string',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Attendant deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Attendant deleted successfully'}
                }
            }
        },
        '404': {
            'description': 'Attendant not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
def delete_attendant(attendant_id):
    try:
        AttendantController.delete_attendant(attendant_id)
        return jsonify({"message": "Attendant deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
