# cli.py
from helpers import (
    exit_program,
    list_doctors,
    find_doctor_by_name,
    create_doctor,
    update_doctor,
    delete_doctor,
    find_patient_by_name,
    create_patient,
    update_patient,
    delete_patient,
    list_patients_by_doctor
)

def main():
    home_options()
    while True:
        user_input = input("Enter your option: ")

        if user_input == "0":
            exit_program()
        elif user_input == "1":
            doctor_submenu()
        elif user_input =="2":
            patient_submenu()
        else:
            print(f"\n{user_input} is not a valid option. Please try again.")
            home_options()

def home_options():
    print("\n***HOME MENU***")
    print("0. Exit program")
    print("1. Doctor menu")
    print("2. Patient menu")

def doctor_submenu():
    while True:
        doctor_options()
        user_input = input("Enter your option: ")

        if user_input == "0":
            home_options()
            break
        elif user_input == "1":
            list_doctors()
        elif user_input == "2":
            find_doctor_by_name()
        elif user_input == "3":
            create_doctor()
        elif user_input == "4":
            update_doctor()
        elif user_input == "5":
            delete_doctor()
        elif user_input == "6":
            list_patients_by_doctor()
        else:
            print(f"\n{user_input} is not a valid option. Please try again.")

def doctor_options():
    print("\n***DOCTOR MENU***")
    print("0. Go Back")
    print("1. List all doctors")
    print("2. Find doctor by name")
    print("3. Create doctor")
    print("4. Update doctor")
    print("5. Delete doctor")
    print("6. List patients by doctor")

def patient_submenu():
    while True:
        patient_options()
        user_input = input("Enter your option: ")

        if user_input == "0":
            home_options()
            break
        elif user_input == "1":
            find_patient_by_name()
        elif user_input == "2":
            create_patient()
        elif user_input == "3":
            update_patient()
        elif user_input == "4":
            delete_patient()
        else:
            print(f"\n{user_input} is not a valid option. Please try again.")
        
def patient_options():
    print("\n***PATIENT MENU***")
    print("0. Go Back")
    print("1. Find patient by name")
    print("2. Create patient")
    print("3. Update patient")
    print("4. Delete patient")

if __name__ == "__main__":
    main()