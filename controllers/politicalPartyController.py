from models.politicalParty import PoliticalParty


class PoliticalPartyController:

    def __init__(self):
        """
        this is the constructor of the politicalPartyController class
        """
        print("Political Party Controller ready")

    def index(self) -> list:
        """
        this method returns all political parties persisted in the db
        :return:
        """
        print("return all Political Parties")

    def show(self, id_: str) -> dict:
        """
        this method return one political party persisted in the db
        :param id_:
        :return:
        """
        print("return one Political Party")

    def create(self, politicalParty_: dict) -> dict:
        """
        this method create one political party
        :param politicalParty_:
        :return:
        """
        print("insert a Political Party")

    def update(self, id_: str, politicalParty_: dict) -> dict:
        """
        update political party registration
        :param id_:
        :param politicalParty_:
        :return:
        """
        print("update an Political Party")

    def delete(self, id_: str) -> str:
        """
        delete political party registration
        :param id_:
        :return:
        """
        print("delete a Political Party")
