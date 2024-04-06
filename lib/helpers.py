from models.doctor import Doctor
from models.patient import Patient

def exit_program():
    print("Goodbye!")
    exit()

# doctor functions

def list_doctors():
    doctors = Doctor.get_all()
    for doctor in doctors:
        print(doctor)

def find_doctor_by_name():
    name = input("Enter doctor's name: ")
    doctor = Doctor.find_by_name(name)
    print(doctor) if doctor else print(
        f'Doctor {name} not found'
    )

def create_doctor():
    name = input(f"Enter name: ")
    type = input(f"Enter doctor type: ")
    try:
        doctor = Doctor.create(name, type)
        print(f"Success: {doctor}")
    except Exception as exc:
        print("Error creating doctor: ", exc)

def update_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        try:
            name = input("Enter the doctor's new name: ")
            doctor.name = name
            type = input("Enter the doctor's practice: ")
            doctor.type = type

            doctor.update()
            print(f"Success: {doctor}")
        except Exception as exc:
            print("Error updating doctor: ", exc)
    else:
        print(f"Doctor {id_} not found")

def delete_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        doctor.delete()
        print(f"Doctor {id_} deleted")
    else:
        print(f"Doctor {id_} not found")

# patient functions

def find_patient_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(
        f"{Patient} not found"
        )
    
def create_patient():
    name = input("Enter the patient's name: ")
    email = input("Enter the patient's email: ")
    doctor_id = input("Enter the patient's doctor(id): ")
    try:
        patient = Patient.create(name, email, int(doctor_id))
        print(f"Success: {patient}")
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        try:
            name = input("Enter the patient's new name: ")
            patient.name = name
            email = input("Enter the patient's new email: ")
            patient.email = email
            doctor_id = input("Enter the patient's new doctor(id): ")
            patient.doctor_id = int(doctor_id)

            patient.update()
            print(f"Success: {patient}")
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f"Patient {id_} not found")

def delete_patient():
    id_ = input("Enter patient's id: ")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f"Patient {id_} deleted")
    else:
        print(f"Patient {id_} not found")

def list_doctor_patients():
    doctor_id = input("Enter the doctor's id: ")
    doctor = Doctor.find_by_id(int(doctor_id))
    if doctor:
        patients = doctor.patients()
        if patients:
            for patient in patients:
                print(patient)
    else:
        print(f"Doctor eith ID {doctor_id} not found")