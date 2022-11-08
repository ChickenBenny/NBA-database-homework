import typing
from connection import DBConnection

class BACKEND:

    def __init__(self):
        self.db_connection = DBConnection()

    def select_from_where(self, column: str, table: str, limitation:str) -> tuple:
        print("success")
        connection, cursor = self.db_connection.get_conn()
        print("success")
        query = f"SELECT {column} FROM {table} WHERE {limitation};"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        self.db_connection.close_conn(connection, cursor)
        return rows

if __name__ == '__main__':
    backend = BACKEND()
    backend.select_from_where("*", "player", "player_ssn='1'")