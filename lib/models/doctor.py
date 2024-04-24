# doctor.py
from models.__init__ import CURSOR, CONN

class Doctor:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, practice, id=None):
        self.id = id
        self.name = name
        self.practice = practice

    def __repr__(self):
        return f"<Doctor {self.id}: {self.name} - {self.practice}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def practice(self):
        return self._practice

    @practice.setter
    def practice(self, practice):
        if isinstance(practice, str) and len(practice):
            self._practice = practice
        else:
            raise ValueError(
                "Practice must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of doctor instances """
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            practice TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists doctor instances """
        sql = """
            DROP TABLE IF EXISTS doctors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and practice values of the current doctor instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO doctors (name, practice)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.practice))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, practice):
        """ Initialize a new doctor instance and save the object to the database """
        doctor = cls(name, practice)
        doctor.save()
        return doctor

    def update(self):
        """Update the table row corresponding to the current doctor instance."""
        sql = """
            UPDATE doctors
            SET name = ?, practice = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.practice, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current doctor instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM doctors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a doctor object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        doctor = cls.all.get(row[0])
        if doctor:
            # ensure attributes match row values in case local instance was modified
            doctor.name = row[1]
            doctor.practice = row[2]

        else:
            # not in dictionary, create new instance and add to dictionary
            doctor = cls(row[1], row[2])
            doctor.id = row[0]
            cls.all[doctor.id] = doctor
        return doctor

    @classmethod
    def get_all(cls):
        """Return a list containing a doctor object per row in the table"""
        sql = """
            SELECT *
            FROM doctors
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a doctor object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM doctors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a doctor object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM doctors
            WHERE name = ?
        """

        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []

    def patients(self):
        """Return list of patients associated with current doctor"""
        from models.patient import Patient
        sql = """
            SELECT * FROM patients
            WHERE doctor_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Patient.instance_from_db(row) for row in rows
        ]