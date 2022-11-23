from flask import Blueprint
from flask import request

from controllers.politicalPartyController import PoliticalPartyController

politicalParty_blueprint = Blueprint('politicalParty_blueprint', __name__)
politicalParty_controller = PoliticalPartyController()


@politicalParty_blueprint.route("/political party/all", methods=['GET'])
def get_politicalParty():
    response = politicalParty_controller.index()
    return response, 200


@politicalParty_blueprint.route("/political party/<string:id_>", methods=['GET'])
def get_politicalParty_by_id(id_):
    response = politicalParty_controller.show(id_)
    return response, 200


@politicalParty_blueprint.route("/political party/insert", methods=['POST'])
def insert_politicalParty():
    politicalParty = request.get_json()
    response = politicalParty_controller.create(politicalParty)
    return response, 201


@politicalParty_blueprint.route("/politicalParty/update/<string:id_>", methods=['PATCH'])
def update_politicalParty(id_):
    politicalParty = request.get_json()
    response = politicalParty_controller.update(id_, politicalParty)
    return response, 201


@politicalParty_blueprint.route("/politicalParty/delete/<string:id_>", methods=['DELETE'])
def delete_politicalParty(id_):
    response = politicalParty_controller.delete(id_)
    return response, 204
