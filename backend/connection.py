import psycopg2

class DBConnection():
    
    def __init__(self):
        self.database = "postgres"
        self.user = "postgres"
        self.password = "postgres"
        self.host = "127.0.0.1"
        self.port = "5432"

    def get_conn(self):
        connection = psycopg2.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )
        cursor = connection.cursor()
        return connection, cursor

    def close_conn(self, connection, cursor):
        cursor.close()
        connection.close()
        print("Close the connection.")