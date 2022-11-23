from flask import Blueprint
from flask import request

from controllers.tableController import TableController

table_blueprint = Blueprint('table_blueprint', __name__)
table_controller = TableController()


@table_blueprint.route("/table/all", methods=['GET'])
def get_table():
    response = table_controller.index()
    return response, 200


@table_blueprint.route("/table/<string:id_>", methods=['GET'])
def get_table_by_id(id_):
    response = table_controller.show(id_)
    return response, 200


@table_blueprint.route("/table/insert", methods=['POST'])
def insert_table():
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprint.route("/table/<string:id_>", methods=['PATCH'])
def update_candidate(id_):
    table = request.get_json()
    response = table_controller.update(id_, table)
    return response, 201

@table_blueprint.route("/table/delete/<string:id_>", methods=['DELETE'])
def delete_table(id_):
    response = table_controller.delete(id_)
    return response, 204
