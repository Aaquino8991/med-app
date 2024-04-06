from helpers import (
    exit_program,
    list_doctors,
    find_doctor_by_name,
    create_doctor,
    update_doctor,
    delete_doctor,
    list_doctor_patients,
    find_patient_by_name,
    create_patient,
    update_patient,
    delete_patient
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_doctors()
        elif choice == "2":
            find_doctor_by_name()
        elif choice == "3":
            create_doctor()
        elif choice == "4":
            update_doctor()
        elif choice == "5":
            delete_doctor()
        elif choice == "6":
            find_patient_by_name()
        elif choice == "7":
            create_patient()
        elif choice == "8":
            update_patient()
        elif choice == "9":
            delete_patient()
        elif choice == "10":
            list_doctor_patients()
        else:
            print("Invalid choice")
        


def menu():
    print("Please select an option:")
    print("0. Exit program")
    print("1. List all doctors")
    print("2. Find doctor by name")
    print("3. Create new doctor")
    print("4. Update doctor information")
    print("5. Delete doctor")
    print("6. Find patient by name")
    print("7. Create new patient")
    print("8. Update patient")
    print("9. Delete patient")
    print("10. List al patients by doctor")


if __name__ == "__main__":
    main()