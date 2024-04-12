from models.doctor import Doctor
from models.patient import Patient
from tabulate import tabulate

def exit_program():
    print("Thank you for using Med App!")
    exit()

# doctor functions

def list_doctors():
    doctors = Doctor.get_all()
    headers = ["Name", "Practice"]
    list = []
    
    for index, doctor in enumerate(doctors):
        doctor_info = (index + 1, doctor.name, doctor.type)
        list.append(doctor_info)
    print(tabulate(list, headers=headers, tablefmt="grid"))
    return doctors    

def find_doctor_by_name():
    name = input("Enter doctor's name: ")
    doctors = Doctor.find_by_name(name)
    headers = ["Name", "Practice"]
    list = []
    for doctor in doctors:
        doctor = (doctor.name, doctor.type)
        list.append(doctor)
    print(tabulate(list, headers=headers, tablefmt="grid"))

def create_doctor():
    name = input(f"Enter name: ")
    type = input(f"Enter doctor type: ")
    try:
        doctor = Doctor.create(name, type)
        print(f"\nSuccess: Doctor {doctor.name} has been created")
    except Exception as exc:
        print("Error creating doctor: ", exc)

def update_doctor():
    doctors = list_doctors()

    index = input("Which doctor do you want to update? (Enter the number in the list): ")
    try:
        index = int(index)
        if 1 <= index <= len(doctors):
            doctor = doctors[index - 1]
            name = input("Enter the doctor's new name: ")
            type_ = input("Enter the doctor's practice: ")
            
            try:
                doctor.name = name
                doctor.type = type_
                doctor.update()
                print(f"Success: Doctor {doctor.name} has been updated")
            except Exception as exc:
                print("Error updating doctor: ", exc)
        else:
            print("Invalid index selected.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_doctor():
    doctors = list_doctors()

    index = int(input("Enter the number in the list or enter 0 to cancel: "))
    if index == 0:
        print("Deletion operation canceled")
        return
    elif 1 <= index <= len(doctors):
        doctor = doctors[index - 1]
        if found_doctor := Doctor.find_by_id(doctor.id):
            found_doctor.delete()
            print(f"Doctor {doctor.name} has been deleted")
        else:
            print(f"Doctor not found")
    else:
        print(f"Invalid number")

def list_patients_by_doctor():
    doctors = list_doctors()
    index = input("Enter the number in the list or enter 0 to cancel: ")
    if index == "0":
        print("Listing patients by doctor canceled")
        return
    try:
        index = int(index)
        if 1 <= index <= len(doctors):
            doctor = doctors[index - 1]
            found_doctor = Doctor.find_by_id(doctor.id)
            if found_doctor:
                patients = found_doctor.patients()
                if patients:
                    headers = ["Name", "Age", "Email", "Doctor"]
                    patient_list = []
                    for patient in patients:
                        patient_info = (patient.name, patient.age, patient.email, found_doctor.name)
                        patient_list.append(patient_info)
                    print(tabulate(patient_list, headers=headers, tablefmt='grid'))
                else:
                    print("No patients found for this doctor.")
            else:
                print("Doctor not found.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number or '0' to cancel.")

# patient functions

def list_patients():
    patients = Patient.get_all()
    headers = ["Name", "Age", "Email", "Doctor"]
    list = []
    
    for index, patient in enumerate(patients):
        patient_info = (index + 1, patient.name, patient.age, patient.email, patient.doctor_id)
        list.append(patient_info)
    print(tabulate(list, headers=headers, tablefmt="grid"))
    return patients    

def find_patient_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(
        f"{Patient} not found"
        )
    
def create_patient():
    name = input("Enter the patient's name: ")
    age = int(input("Enter patient's age: "))
    email = input("Enter the patient's email: ")
    doctor_id = input("Enter the patient's doctor(id): ")
    try:
        patient = Patient.create(name, age, email, int(doctor_id))
        print(f"Success: {patient}")
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    list_patients()
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        try:
            name = input("Enter the patient's new name: ")
            patient.name = name
            age = input("Enter patient's new age: ")
            patient.age = int(age)
            email = input("Enter the patient's new email: ")
            patient.email = email
            doctor_id = input("Enter the patient's new doctor(id): ")
            patient.doctor_id = int(doctor_id)

            patient.update()
            print(f"Success: {patient.name} has been added as a patient")
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