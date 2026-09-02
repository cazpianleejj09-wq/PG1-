
from flask import Flask, request, jsonify, render_template

from backend import (
    register_patient,
    book_appointment,
    calculate_bill,
    assign_triage_room
)


app = Flask(__name__)


# Display the frontend
@app.route("/")
def home():

    return render_template("index.html")


# Register Patient
@app.route("/register", methods=["POST"])
def register():

    data = request.json

    result = register_patient(
        data.get("name"),
        data.get("age"),
        data.get("id")
    )

    return jsonify(result)


# Book Appointment
@app.route("/appointment", methods=["POST"])
def appointment():

    data = request.json

    result = book_appointment(
        data.get("department"),
        data.get("appointment_date"),
        data.get("confirmation")
    )

    return jsonify(result)


# Calculate Bill
@app.route("/bill", methods=["POST"])
def bill():

    data = request.json

    result = calculate_bill(
        data.get("patient_type"),
        data.get("number_of_tests")
    )

    return jsonify(result)


# Assign Triage Room
@app.route("/triage", methods=["POST"])
def triage():

    data = request.json

    result = assign_triage_room(
        data.get("severity")
    )

    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)

