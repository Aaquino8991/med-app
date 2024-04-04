from models.__init__ import CURSOR, CONN

class Doctor():
    
    def __init__(self, name, type, phone, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.phone = phone

    @classmethod
    def create_table(cls):
        """Create new table to persist attributes of Doctor instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            phone TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Delete table"""
        sql = """
            DROP TABLE IF EXISTS doctors;
        """
        CURSOR.execute(sql)
        CONN.commit()