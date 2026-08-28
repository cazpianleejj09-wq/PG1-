from datetime import date, timedelta
from datetime import datetime


department = input("Enter department (GP/Specialist): ").strip()

while department.lower() not in ["gp", "specialist"]:
        print("Invalid department, please re-enter.")
        department = input("Enter department (GP/Specialist): ").strip()

    # Get valid appointment date
while True:
        appointment_date = input("Enter appointment date (DD/MM/YYYY): ").strip()

        try:
            appointment_date = datetime.strptime(
                appointment_date, "%d/%m/%Y"
            ).date()

            today = date.today()
            latest_date = today + timedelta(days=7)

            if today <= appointment_date <= latest_date:
                break
            else:
                print("Invalid date. Appointment must be within the next 7 days.")

        except ValueError:
            print("Invalid date format. Please enter DD/MM/YYYY.")

    # Confirm booking
confirmation = input("Confirm booking? (Y/N): ").strip()

if confirmation.upper() == "Y":
        print("\nBooking confirmed!")
        print("Department:", department.title())
        print("Appointment date:", appointment_date.strftime("%d/%m/%Y"))

else:
        print("Booking cancelled.")
