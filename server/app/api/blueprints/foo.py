from flask import Blueprint, jsonify, request
from sqlalchemy import exc
from app import db
from app.api.models.foo import Foo

foo_blueprint = Blueprint('foo', __name__)


@foo_blueprint.route('/api/foo', methods=['POST'])
def post():

    response_object = {
        'errors': ['Invalid request.']
    }

    # Handle invalid input
    post_data = request.get_json()
    if not post_data:
        return jsonify(response_object), 400

    # Get request data
    string_field = post_data.get('string_field')

    # Optional check if object already exists in database
    if (len(Foo.query.filter_by(string_field=string_field).all()) > 0):
        response_object = {
            'errors': [f'String "{string_field}" already exists']
        }
        return jsonify(response_object), 400

    # Add to DB
    foo_row = Foo(string_field=string_field)
    db.session.add(foo_row)
    db.session.commit()

    # Return success and created object
    response_object = {
        'foo': foo_row.to_json()
    }
    return jsonify(response_object), 201


@foo_blueprint.route('/api/foo', methods=['GET'])
def get():
    response_object = {
        'records': [foos.to_json() for foos in Foo.query.all()]
    }
    return jsonify(response_object), 200


@foo_blueprint.route('/api/foo', methods=['PUT'])
def put():

    response_object = {
        'errors': ['Invalid request.']
    }

    # Handle invalid input
    put_data = request.get_json()
    if not put_data:
        return jsonify(response_object), 400

    # Get request data
    foo_id = put_data.get('id')
    new_string_field = put_data.get('string_field')

    # Check that the table has an entry with that id. If not, throw error
    record_to_modify = Foo.query.filter_by(id=foo_id).first()
    if not record_to_modify:
        response_object = {
            'errors': [f'No record with id={foo_id} found.']
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
        'foo': record_to_modify.to_json()
    }
    return jsonify(response_object), 200


@foo_blueprint.route('/api/foo', methods=['DELETE'])
def delete():

    response_object = {
        'errors': ['Invalid request.']
    }

    # Handle invalid input
    delete_data = request.get_json()
    if not delete_data:
        return jsonify(response_object), 400

    # Get request data
    foo_id = delete_data.get('id')

    # Check that the table has an entry with that id. If not, throw error
    record_to_delete = Foo.query.filter_by(id=foo_id).first()
    if not record_to_delete:
        response_object = {
            'errors': [f'No record with id={foo_id} found.']
        }
        return jsonify(response_object), 400

    # Detete the record
    db.session.delete(record_to_delete)
    db.session.commit()

    # Return success
    response_object = { }
    return jsonify(response_object), 200
