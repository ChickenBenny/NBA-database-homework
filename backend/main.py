import typing
from connection import DBConnection

class BACKEND:

    def __init__(self):
        self.db_connection = DBConnection()

    

    def select_from_where(self, column: str, table: str, limit:str) -> tuple:
        connection, cursor = self.db_connection.get_conn()
        query = f"SELECT {column} FROM {table} WHERE {limit};"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.db_connection.close_conn(connection, cursor)
        return rows

    def delete(self, table: str, limit: str) -> None:
        connection, cursor = self.db_connection.get_conn()
        query = f"DELETE FROM {table} WHERE {limit};"
        cursor.execute(query)
        connection.commit()
        self.db_connection.close_conn(connection, cursor)

    def insert(self, table: str, info: str) -> None:
        connection, cursor = self.db_connection.get_conn()
        query = f"INSERT INTO {table} VALUES({info});"
        cursor.execute(query)
        connection.commit()
        self.db_connection.close_conn(connection, cursor) 

    def update(self, table: str, setting: str, limit: str) -> None:
        connection, cursor = self.db_connection.get_conn()
        query = f"UPDATE {table} SET {setting} WHERE {limit};"
        cursor.execute(query)
        connection.commit()
        self.db_connection.close_conn(connection, cursor) 




if __name__ == '__main__':
    backend = BACKEND()
    backend.select_from_where("*", "player", "player_ssn='1'")
    backend.delete("player", "player_ssn='31'")
    backend.insert("player", "'31', 'Benny', 'Hsiao', '4', '2'")
    backend.update("player", "current_team='5'", "player_ssn='31'")