# helpers.py
from models.doctor import Doctor
from models.patient import Patient
from tabulate import tabulate
import re

def exit_program():
    print("Thank you for using Med App!")
    exit()

# doctor functions

def list_doctors():
    doctors = Doctor.get_all()
    headers = ["Name", "Practice"]
    list = []
    
    for index, doctor in enumerate(doctors):
        doctor_info = (index + 1, doctor.name, doctor.practice)
        list.append(doctor_info)
    print(tabulate(list, headers=headers, tablefmt="grid"))
    return doctors    

def find_doctor_by_name():
    name = input("Enter doctor's name: ")
    doctors = Doctor.find_by_name(name)
    headers = ["Name", "Practice"]
    list = []
    for doctor in doctors:
        doctor = (doctor.name, doctor.practice)
        list.append(doctor)
    print(tabulate(list, headers=headers, tablefmt="grid"))

def create_doctor():

    name = input(f"Enter name: ")
    practice = input(f"Enter doctor's practice: ")

    pattern = "^[a-zA-Z]+$"
    
    if not re.match(pattern, name):
        print("Error: Name can only contain letters.")
        return
    
    if not re.match(pattern, practice):
        print("Error: Type can only contain letters.")
        return
    
    try:
        doctor = Doctor.create(name, practice)
        print(f"\nSuccess: Doctor {doctor.name} has been created")
    except Exception as exc:
        print("\nError creating doctor: ", exc)

def update_doctor():
    doctors = list_doctors()

    index = int(input("""
Which doctor do you want to update? 
(Enter the number in the list or 0 to cancel): 
"""))
    try:
        if index == 0:
            print("\nUPDATE CANCELED")
            return
        if 1 <= index <= len(doctors):
            doctor = doctors[index - 1]
            name = input("Enter the doctor's new name: ")
            practice_ = input("Enter the doctor's practice: ")

            pattern = "^[a-zA-Z]+$"

            if not re.match(pattern, name):
                print("Name can only be letters")
                return

            if not re.match(pattern, practice_):
                print("Practice can only be letters")
                return
            
            try:
                doctor.name = name
                doctor.practice = practice_
                doctor.update()
                print(f"\nSuccess: Doctor {doctor.name} has been updated")
            except Exception as exc:
                print("\nError updating doctor: ", exc)
        else:
            print("\nInvalid index selected.")
    except ValueError:
        print("\n***INVALID INPUT***. Please enter a number.")

def delete_doctor():
    doctors = list_doctors()

    try:
        index = int(input("\nEnter the number in the list or enter 0 to cancel: "))
        if index == 0:
            print("\nDELETION OPERATION CANCELED")
            return
        elif 1 <= index <= len(doctors):
            doctor = doctors[index - 1]
            found_doctor = Doctor.find_by_id(doctor.id)
            found_doctor.delete()
            print(f"\nDoctor {doctor.name} has been deleted")
        else:
            print(f"\n***INVALID NUMBER***. Please enter a number in the list.")
            delete_doctor()
    except ValueError:
        print("\n***INVALID INPUT***. Please enter a number in the list.")
        delete_doctor()

def list_patients_by_doctor():
    doctors = list_doctors()
    
    try:
        index = int(input("Enter the number in the list or enter 0 to cancel: "))
        if index == 0:
            print("OPERATION CANCELED")
            return
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
        print("""\n***INVALID INPUT*** 
Please enter a number or '0' to cancel.""")
        list_patients_by_doctor()

# patient functions

def list_patients():
    patients = Patient.get_all()
    headers = ["Name", "Age", "Email", "Doctor"]
    list = []
    for index, patient in enumerate(patients):
        doctor = Doctor.find_by_id(patient.doctor_id)
        patient_info = (index + 1, patient.name, patient.age, patient.email, doctor.name)
        list.append(patient_info)
    print(tabulate(list, headers=headers, tablefmt="grid"))
    return patients    

def find_patient_by_name():
    name = input("Enter patient's name: ")
    patient = Patient.find_by_name(name)
    headers = ["Name", "Age", "Email", "Doctor"]
    list = []
    if patient:
        doctor = Doctor.find_by_id(patient.doctor_id)
        doctor_name = doctor.name if doctor else "Unknown Doctor"
        patient_info = (patient.name, patient.age, patient.email, doctor_name)
        list.append(patient_info)
        print(tabulate(list, headers=headers, tablefmt="grid"))
    else:
        print("Patient not found")

def create_patient():
    name = input("Enter the patient's name: ")
    age = int(input("Enter patient's age: "))
    email = input("Enter the patient's email: ")

    doctors = list_doctors()
    doctor_choices = [str(i + 1) for i in range(len(doctors))]
    doctor_choice = input("Choose the doctor by entering the corresponding number: ")

    try:
        if doctor_choice in doctor_choices:
            selected_doctor = doctors[int(doctor_choice) - 1]
            doctor_id = selected_doctor.id
            try:
                patient = Patient.create(name, age, email, doctor_id)
                print(f"Success: {patient.name} has been created")
            except Exception as exc:
                print("Error creating patient: ", exc)
        else:
            print("Invalid doctor choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_patient():
    patients = list_patients()

    index = int(input("""
Which patient do you want to update? 
(Enter the number in the list or 0 to exit): """))
    
    try:
        if index == 0:
            print("UPDATE CANCELED")
            return
        if 1 <= index <= len(patients):
            patient = patients[index - 1]
            name = input("Enter the patient's new name: ")
            age = int(input("Enter the patient's age: "))
            email = input("Enter the patient's new email: ")
            
            print("\nSelect the new doctor:")
            doctors = list_doctors()

            doctor_choice = int(input("\nChoose the doctor by entering the corresponding number: "))

            if 1 <= doctor_choice <= len(doctors):
                selected_doctor = doctors[doctor_choice - 1]
                doctor_id = selected_doctor.id
                
                try:
                    patient.name = name
                    patient.age = age
                    patient.email = email
                    patient.doctor_id = doctor_id
                    patient.update()
                    print(f"Success: Patient {patient.name} has been updated")
                except Exception as exc:
                    print("Error updating patient: ", exc)
            else:
                print("Invalid doctor choice.")
        else:
            print("Invalid index selected.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_patient():
    patients = list_patients()
    
    try:
        index = int(input("Which patient would you like to delete: "))
        if index == 0:
            print("OPERATION CANCELED")
            return
        elif 1 <= index <= len(patients):
            patient = patients[index - 1]
            if found_patient := Patient.find_by_id(patient.id):
                found_patient.delete()
                print("Patient has been deleted")
            else:
                print("Patient not found")
        else:
            print("Invalid index entered")
    except ValueError:
        print("Invalid input. Please enter a number.")