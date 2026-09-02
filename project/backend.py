from datetime import date, timedelta, datetime


def calculate_bill(patient_type, number_of_tests):
    # Validate patient type
    patient_type = patient_type.lower()

    if patient_type not in ["subsidised", "private"]:
        return {
            "success": False,
            "message": "Patient type must be subsidised or private."
        }

    # Validate number of tests
    if not isinstance(number_of_tests, int) or number_of_tests < 0:
        return {
            "success": False,
            "message": "Number of tests must be 0 or more."
        }

    # Fees
    base_consultation_fee = 100.00
    lab_test_rate = 10.00

    # Calculate subtotal
    subtotal = base_consultation_fee + (
        number_of_tests * lab_test_rate
    )

    # Calculate total
    if patient_type == "subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    return {
        "success": True,
        "patient_type": patient_type,
        "number_of_tests": number_of_tests,
        "subtotal": round(subtotal, 2),
        "total": round(total, 2)
    }


def assign_triage_room(severity):
    # Validate severity
    if not isinstance(severity, int) or severity < 1 or severity > 10:
        return {
            "success": False,
            "message": "Severity must be a whole number from 1 to 10."
        }

    # Assign room
    if 1 <= severity <= 4:
        room = "Waiting Room"
    elif 5 <= severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    return {
        "success": True,
        "severity": severity,
        "assigned_room": room
    }


def register_patient(patient_name, patient_age, patient_id):
    # Validate name
    if not patient_name or patient_name.strip() == "":
        return {
            "success": False,
            "message": "Patient name cannot be empty."
        }

    # Validate age
    if not isinstance(patient_age, int) or patient_age <= 0:
        return {
            "success": False,
            "message": "Patient age must be greater than 0."
        }

    # Validate ID
    if not isinstance(patient_id, int) or patient_id < 0:
        return {
            "success": False,
            "message": "Patient ID cannot be negative."
        }

    return {
        "success": True,
        "message": "Patient registered successfully.",
        "patient": {
            "name": patient_name,
            "age": patient_age,
            "id": patient_id
        }
    }


def book_appointment(department, appointment_date, confirmation):
    # Validate department
    department = department.strip().lower()

    if department not in ["gp", "specialist"]:
        return {
            "success": False,
            "message": "Department must be GP or Specialist."
        }

    # Validate confirmation
    if confirmation.upper() != "Y":
        return {
            "success": False,
            "message": "Booking cancelled."
        }

    # Convert date
    try:
        appointment_date = datetime.strptime(
            appointment_date,
            "%d/%m/%Y"
        ).date()
    except ValueError:
        return {
            "success": False,
            "message": "Invalid date format. Please use DD/MM/YYYY."
        }

    # Check date range
    today = date.today()
    latest_date = today + timedelta(days=7)

    if not today <= appointment_date <= latest_date:
        return {
            "success": False,
            "message": "Appointment must be within the next 7 days."
        }

    return {
        "success": True,
        "message": "Booking confirmed!",
        "department": department.title(),
        "appointment_date": appointment_date.strftime("%d/%m/%Y")
    }