from models.__init__ import CURSOR, CONN
from models.doctor import Doctor
from models.patient import Patient

def seed_database():
    Patient.drop_table()
    Doctor.drop_table()
    Patient.create_table()
    Doctor.create_table()

    john = Doctor.create("John", "Oncologist")
    wylie = Doctor.create("Wylie", "Orthopedic Surgeon")
    kim = Doctor.create("Kim", "Family Medicine")
    greenefield = Doctor.create("Greenefield", "Pediatrician")

    Patient.create("Anthony", "anthony@myemail.com", wylie.id)
    Patient.create("Lissette", "lissette@myemail.com", kim.id)
    Patient.create("Alina", "alina@myemail.com", greenefield.id)
    Patient.create("Liam", "liam@myemail.com", greenefield.id)
    Patient.create("Fernando", "fernando@myemail.com", john.id)

seed_database()
print("Seeded database")