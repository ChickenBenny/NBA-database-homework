
from backend.connection import DBConnection

db_connection = DBConnection()

def select_from_where(column: str, table: str, limit:str) -> tuple:
    connection, cursor = db_connection.get_conn()
    query = f"SELECT {column} FROM {table} WHERE {limit};"
    cursor.execute(query)
    rows = cursor.fetchall()
    db_connection.close_conn(connection, cursor)
    return rows

def delete(table: str, limit: str) -> None:
    connection, cursor = db_connection.get_conn()
    query = f"DELETE FROM {table} WHERE {limit};"
    cursor.execute(query)
    connection.commit()
    db_connection.close_conn(connection, cursor)

def insert(table: str, info: str) -> None:
    connection, cursor = db_connection.get_conn()
    query = f"INSERT INTO {table} VALUES({info});"
    cursor.execute(query)
    connection.commit()
    db_connection.close_conn(connection, cursor) 

def update(table: str, info: str, limit: str) -> None:
    connection, cursor = db_connection.get_conn()
    query = f"UPDATE {table} SET {info} WHERE {limit};"
    cursor.execute(query)
    connection.commit()
    db_connection.close_conn(connection, cursor) 




if __name__ == '__main__':
    select_from_where("*", "player", "player_ssn='1'")
    delete("player", "player_ssn='31'")
    insert("player", "'31', 'Benny', 'Hsiao', '4', '2'")
    update("player", "current_team='5'", "player_ssn='31'")