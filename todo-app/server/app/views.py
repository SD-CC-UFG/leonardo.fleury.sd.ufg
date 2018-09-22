from flask import Blueprint, abort, request, jsonify
from .models import TodoItem

todo_page = Blueprint('todo_page', __name__)

@todo_page.route('/')
def get_todos():
    itens = TodoItem.get_all()
    results = []

    for item in itens:
        obj = {
            'id': item.id,
            'content': item.content,
            'date_created': item.date_created,
            'date_modified': item.date_modified
        }
        results.append(obj)

    response = jsonify(results)
    response.status_code = 200
    return response

@todo_page.route('/', methods=["POST"])
def create_todo():
    if request.is_json:
        data = request.get_json()
        item = TodoItem(data['content'])
        item.save()

        response = jsonify({
            'id': item.id,
            'content': item.content,
            'date_created': item.date_created,
            'date_modified': item.date_modified
        })
        response.status_code = 201
        return response

    else:
        response = jsonify({ 'error': 'Request is not a JSON'})
        response.status_code = 400
        return response

@todo_page.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    if request.is_json:
        item = TodoItem.query.filter_by(id=id).first()
        data = request.get_json()
        
        if not item:
            abort(404)

        item.content = data['content']
        item.save()

        response = jsonify({
            'id': item.id,
            'content': item.content,
            'date_created': item.date_created,
            'date_modified': item.date_modified
        })
        response.status_code = 201
        return response

    else:
        response = jsonify({ 'error': 'Request is not a JSON'})
        response.status_code = 400
        return response

@todo_page.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    item = TodoItem.query.filter_by(id=id).first()
    item.delete()

    return {
        "message": "Todo {} apagado".format(id)
    }, 200