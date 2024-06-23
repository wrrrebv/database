from database import Database

class Deliveries:

    @staticmethod
    def get_by_id(delivery_id: int):
        stmt = 'SELECT * FROM delivery WHERE id=%s;'
        Database.cursor().execute(stmt, [delivery_id])
        return Database.cursor().fetchone()

    @staticmethod
    def get_by_departure_city(departure_city: str):
        stmt = 'SELECT * FROM delivery WHERE departure_city=%s'
        Database.cursor().execute(stmt, [departure_city])
        return Database.cursor().fetchall()

    @staticmethod
    def get_all(order_col: str = 'name', order_ascending: bool = True):
        order = 'ASC' if order_ascending else 'DESC'
        stmt = f'SELECT * FROM city ORDER BY {order_col} {order}'
        Database.cursor().execute(stmt, [])
        return Database.cursor().fetchall()

    @staticmethod
    def get_column_names():
        stmt = 'SHOW COLUMNS FROM delivery;'
        Database.cursor().execute