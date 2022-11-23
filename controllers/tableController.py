from models.table import Table


class TableController:

    def __init__(self):
        """
        this is the constructor of the TableController class
        """
        print("Table Controller ready")

    def index(self) -> list:
        """
        this method returns all tables persisted in the db
        :return:
        """
        print("return all tables")

    def show(self, id_: str) -> dict:
        """
        this method return one table persisted in the db
        :param self:
        :param id_:
        :return:
        """
        print("return one table")

    def create(self, table_: dict) -> dict:
        """
        this method create one table
        :param table_:
        :return:
        """
        print("insert a table")

    def update(self, id_: str, table_: dict) -> dict:
        """
        update table registration
        :param id_:
        :param table_:
        :return:
        """
        print("update an table")

    def delete(self, id_: str) -> str:
        """
        delete table registration
        :param id_:
        :return:
        """
        print("delete a table")
