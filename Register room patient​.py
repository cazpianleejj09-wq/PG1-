def register_patient():
    Patient_Name = input("Enter Patient Name: ")

    while Patient_Name == "":
        print("Error")
        Patient_Name = input("Enter Patient Name: ")

    Patient_Age = int(input("Enter Patient Age: "))

    while Patient_Age <= 0:
        print("Error")
        Patient_Age = int(input("Enter Patient Age: "))

    Patient_ID = int(input("Enter Patient ID: "))

    while Patient_ID < 0:
        print("Error")
        Patient_ID = int(input("Enter Patient ID: "))

    print("Patient details confirmed")
    print("Patient Name:", Patient_Name)
    print("Patient Age:", Patient_Age)
    print("Patient ID:", Patient_ID)
    print("Success")


# Call the function
register_patient()