from flask import Blueprint, request, jsonify
from app.services import get_users, get_user_by_id
from app.utils import bad_request, not_found

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET'])
def list_users():
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        q = request.args.get('q', None)
        role = request.args.get('role', None)
        is_active = request.args.get('is_active', None)
        if is_active is not None:
            if is_active.lower() == 'true':
                is_active = True
            elif is_active.lower() == 'false':
                is_active = False
            else:
                return bad_request("Invalid value for is_active. Use true or false.")
    except ValueError:
        return bad_request("Invalid query parameters.")

    if page_size > 50:
        return bad_request("page_size cannot be greater than 50.")

    result = get_users(page=page, page_size=page_size, q=q, role=role, is_active=is_active)
    return jsonify(result), 200

@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return not_found("User not found")
    return jsonify({"data": user}), 200