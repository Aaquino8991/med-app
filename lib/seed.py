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

    Patient.create("Anthony", 35, "anthony@myemail.com", wylie.id)
    Patient.create("Lissette", 32, "lissette@myemail.com", kim.id)
    Patient.create("Alina", 7, "alina@myemail.com", greenefield.id)
    Patient.create("Liam", 4, "liam@myemail.com", greenefield.id)
    Patient.create("Fernando", 29, "fernando@myemail.com", john.id)

seed_database()
print("Seeded database")