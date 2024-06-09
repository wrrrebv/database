import mysql.connector


class Database:
    __connection = mysql.connector.connect(user='root', host='localhost', port='3306', password='20232023', database='world')
    __cursor = __connection.cursor(prepared=True)

    @classmethod
    def cursor(cls):
        return cls.__cursor
