import curses
from datetime import date, timedelta
from datetime import datetime
def calculate_bill():
    print("What type of patient?")
    patient_type = input("Enter subsidised or private: ").lower()

    while patient_type != "subsidised" and patient_type != "private":
        print("Invalid patient type. Please enter subsidised or private.")
        patient_type = input("Enter subsidised or private: ").lower()

    print("How many lab tests were completed?")
    number_of_tests = int(input("Enter number of tests: "))

    while number_of_tests < 0:
        print("Invalid number. Please enter a valid number.")
        number_of_tests = int(input("Enter number of tests: "))

    # Set the fees
    base_consultation_fee = 100.00
    lab_test_rate = 10.00

    # Calculate subtotal
    subtotal = base_consultation_fee + (number_of_tests * lab_test_rate)

    # Calculate total based on patient type
    if patient_type == "subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    # Display results
    print("Patient Type:", patient_type)
    print("Total: $", format(total, ".2f"))
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
def book_appointment():
    print("Welcome to the Appointment Booking System")

    # Get valid department input
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
 





menu = [
    "Register patient",
    "Book appointment",
    "Calculate bill",
    "Assign Triage room",
    "Exit"
]


# Functions assigned to each menu option
functions = [
    register_patient,
    book_appointment,
    calculate_bill,
    assign_triage_room
]


def draw_menu(stdscr, selected_row):
    stdscr.clear()

    # Title
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(0, 5, "===== MAIN MENU =====")
    stdscr.attroff(curses.color_pair(2))

    # Menu options
    for i, item in enumerate(menu):

        if i == selected_row:
            # Selected option
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(i + 2, 5, f"> {i + 1}. {item}")
            stdscr.attroff(curses.color_pair(1))

        else:
            # Normal option
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(i + 2, 5, f"  {i + 1}. {item}")
            stdscr.attroff(curses.color_pair(3))

    # Instructions
    stdscr.addstr(8, 5, "Use ↑ and ↓ to navigate.")
    stdscr.addstr(9, 5, "Press ENTER to select.")

    stdscr.refresh()


def main(stdscr):

    curses.curs_set(0)
    curses.start_color()

    # Colours
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)

    # White background
    stdscr.bkgd(" ", curses.color_pair(2))

    current_row = 0

    while True:

        draw_menu(stdscr, current_row)

        key = stdscr.getch()

        # Move up
        if key == curses.KEY_UP:
            current_row = (current_row - 1) % len(menu)

        # Move down
        elif key == curses.KEY_DOWN:
            current_row = (current_row + 1) % len(menu)

        # Enter
        elif key == 10:

            # Exit
            if current_row == 4:
                print("Thank you for using the system. Goodbye!")
                break

            # Call the function assigned to the selected option
            else:
                curses.endwin()  # End curses mode before executing the function
                functions[current_row]()
                input("Press ENTER to continue...")

curses.wrapper(main)

