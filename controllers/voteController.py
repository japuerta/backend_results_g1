from models.vote import Vote


class VoteController:

    def __init__(self):
        """
        this is the constructor of the VoteController class
        """
        print("Vote Controller ready")

    def index(self) -> list:
        """
        this method returns all votes persisted in the db
        :return:
        """
        print ("return all votes")

    def show(self, id_: str) -> dict:
        """
        this method return one vote persisted in the db
        :param id_:
        :return:
        """
        print ("return one vote")

    def create(self, vote_: dict) -> dict:
        """
        this method create one vote
        :param vote_:
        :return:
        """
        print ("insert a vote")

    def update(self, id_: str, vote_: dict) -> dict:
        """
        update vote registration
        :param id_:
        :param vote_:
        :return:
        """
        print("update an vote")

    def delete(self, id_: str) -> str:
        """
        delete table registration
        :param id_:
        :return:
        """
        print("delete a vote")
