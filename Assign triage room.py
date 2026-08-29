def assign_triage_room():
    severity_input = input("Enter severity of condition (1-10): ")

    while not severity_input.isdigit() or int(severity_input) < 1 or int(severity_input) > 10:
        print("Invalid input. Please enter a whole number between 1 and 10.")
        severity_input = input("Enter severity of condition (1-10): ")

    severity = int(severity_input)

    if severity >= 1 and severity <= 4:
        room = "Waiting Room"
    elif severity >= 5 and severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    print("Triage Summary:")
    print("Severity Level:", severity)
    print("Assigned Room:", room)


assign_triage_room()