from models.candidate import Candidate


class CandidateController:

    def __init__(self):
        """
        this is the constructor of the candidateController class
        """
        print("Candidate Controller ready")

    def index(self) -> list:
        """
        this method returns all candidates persisted in the db
        :return: candidate´s list
        """
        print("return all candidates")
        data = {
            "id_": "abc123",
            "personal_id": "123456",
            "names": "alvaro",
            "last name": "perez",
            "political party": "liberal"
        }
        candidate = Candidate(data)
        return [candidate.__dict__]

    def show(self, id_: str) -> dict:
        """
        this method return one candidate persisted in the db
        :param id_:
        :return: one candidate
        """
        print("return one candidate")
        data = {
            "id_": id_,
            "personal_id": "123456",
            "names": "alvaro",
            "last name": "perez",
            "political party": "liberal"
        }
        candidate = Candidate(data)
        return candidate.__dict__

    def create(self, candidate_: dict) -> dict:
        """
        this method create one candidate
        :param candidate_:
        :return: insert one candidate
        """
        print("insert a candidate")
        candidate = Candidate(candidate_)
        return candidate.__dict__

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        :param id_:
        :param candidate_:
        :return: update candidate registration
        """
        print("update an candidate")
        data = candidate_
        data['_id'] = id_
        candidate = Candidate(data)
        return candidate.__dict__

    def delete(self, id_: str) -> dict:
        """
        :param id_:
        :return: delete candidate registration
        """
        print("delete a candidate" + id_)
        return {"delete count": 1}
