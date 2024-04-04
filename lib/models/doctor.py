from models.__init__ import CURSOR, CONN

class Doctor():
    
    def __init__(self, name, type, phone, email, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.phone = phone
        self.email = email

    @classmethod
    def create_table(cls):
        """Create new table to persist attributes of Doctor instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            phone TEXT,
            email TEXT
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

    def save(self):
        """Insert a new row with the values of the corresponding attributes"""
        CURSOR.execute(
            """INSERT INTO doctors (name, type, phone, email) 
               VALUES (?, ?, ?, ?)""",
            (self.name, self.type, self.phone, self.email)
        )
        CONN.commit()

    @classmethod
    def create(cls, name, type, phone, email):
        doctor = cls(name, type, phone, email)
        doctor.save()
        return doctor