from flask import Blueprint, jsonify, request
from sqlalchemy import exc
from main import db
from main.api.models import ExampleTable

example_blueprint = Blueprint('example', __name__)

# TODO add a param passed variable to the api handling


# Example get, post, put, delete endpoint
@example_blueprint.route('/api/example_endpoint', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_post_put_delete_example():
    # Default error response
    response_object = {
        'errors': ['Invalid request.']
    }

    if request.method == 'GET':
        # TODO Return all example_table records
        # TODO if argument provided return that many example_table records
        response_object = {
            'examples': [examples.to_json() for examples in ExampleTable.query.all()]
        }
        return jsonify(response_object), 200

    if request.method == 'POST':
        # Handle invalid input
        post_data = request.get_json()
        if not post_data:
            return jsonify(response_object), 400

        # Get request data
        string_field = post_data.get('string_field')

        # Optional check if object already exists in database
        if (len(ExampleTable.query.filter_by(string_field=string_field).all()) > 0):
            response_object = {
                'errors': [f'Example String "{string_field}" already exists']
            }
            return jsonify(response_object), 400

        # Add to DB
        example_row = ExampleTable(string_field=string_field)
        db.session.add(example_row)
        db.session.commit()

        # Return success and created object
        response_object = {
            'status': 'Successfully created an example row.',
            'example': example_row.to_json()
        }
        return jsonify(response_object), 201

    # Update the example table via it's id
    if request.method == 'PUT':
        # Handle invalid input
        put_data = request.get_json()
        if not put_data:
            return jsonify(response_object), 400

        # Get request data
        example_id = put_data.get('id')
        new_string_field = put_data.get('string_field')

        # Check that the table has an entry with that id. If not, throw error
        record_to_modify = ExampleTable.query.filter_by(id=example_id).first()
        if not record_to_modify:
            response_object = {
                'errors': [f'No record with id={example_id} found.']
            }
            return jsonify(response_object), 400

        if type(new_string_field) is not str:
            response_object = {
                'errors': ['The string_field must be a string.']
            }
            return jsonify(response_object), 400

        record_to_modify.string_field = new_string_field
        db.session.commit()

        # Return success and updated object
        response_object = {
            'status': 'Successfully updated Example string field.',
            'example': record_to_modify.to_json()
        }
        return jsonify(response_object), 200

    # Remove an object with that id
    if request.method == 'DELETE':
        # Handle invalid input
        delete_data = request.get_json()
        if not delete_data:
            return jsonify(response_object), 400

        # Get request data
        example_id = delete_data.get('id')

        # Check that the table has an entry with that id. If not, throw error
        record_to_delete = ExampleTable.query.filter_by(id=example_id).first()
        if not record_to_delete:
            response_object = {
                'errors': [f'No record with id={example_id} found.']
            }
            return jsonify(response_object), 400

        # Detete the record
        db.session.delete(record_to_delete)
        db.session.commit()

        # Return success
        response_object = {
            'status': 'Successfully deleted that object.'
        }
        return jsonify(response_object), 200

    # If no valid request
    return jsonify(response_object), 400
