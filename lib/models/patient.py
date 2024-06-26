# patient.py
from models.__init__ import CURSOR, CONN
from models.doctor import Doctor

class Patient:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, age, email, doctor_id, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"<Patient {self.id}: {self.name} | {self.age} | {self.email} | {self.doctor_id}>"

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            raise ValueError(
                "Email must be a non-empty string"
            )
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and int(age > 0):
            self._age = age
        else:
            raise ValueError(
                "Age must be a number greater than 0"
            )

    @property
    def doctor_id(self):
        return self._doctor_id
    
    def doctor_id(self, doctor_id):
        if doctor_id is None:
            self._doctor_id = None
            self._doctor_name = "Unknown doctor"
        elif isinstance(doctor_id, int):
            doctor = Doctor.find_by_id(doctor_id)
            if doctor:
                self._doctor_id = doctor_id
                self._doctor_name = doctor.name
            else:
                raise ValueError("doctor_id must reference a doctor in the database")
        else:
            raise ValueError("doctor_id must be an integer or None")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Patient instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT,
            doctor_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Patient instances """
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and doctor id values of the current Patient object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO patients (name, age, email, doctor_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.email, self.doctor_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Patient instance."""
        sql = """
            UPDATE patients
            SET name = ?, age = ?, email = ?, doctor_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.email,
                             self.doctor_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Patient instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM patients
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, age, email, doctor_id):
        """ Initialize a new Patient instance and mapping the object to the database """
        patient = cls(name, age, email, doctor_id)
        patient.save()
        return patient

    @classmethod
    def instance_from_db(cls, row):
        """Return an Patient object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        patient = cls.all.get(row[0])
        if patient:
            # ensure attributes match row values in case local instance was modified
            patient.name = row[1]
            patient.age = row[2]
            patient.email = row[3]
            patient.doctor_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            patient = cls(row[1], row[2], row[3], row[4])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient

    @classmethod
    def get_all(cls):
        """Return a list containing one Patient object per table row"""
        sql = """
            SELECT *
            FROM patients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Patient object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM patients
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Patient object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM patients
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None