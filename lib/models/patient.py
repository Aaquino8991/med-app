from models.__init__ import CURSOR, CONN

class Patient:

    def __init__(self, name, sex, address, email, id=None):
        self.id = id
        self.name = name
        self.sex = sex
        self.address = address
        self.email = email

    @classmethod
    def create_table(cls):
        """Create table to persist attributes of Patient instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            sex TEXT,
            address TEXT,
            email TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Delete table"""
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()