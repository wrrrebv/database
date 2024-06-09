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