from flask import render_template

def list_pacientes(pacientes):
    print(pacientes)
    return render_template("patients.html",patients=pacientes)
def create_pacientes():
    return render_template("create_patients.html")
def update_paciente(pacientes):
    return render_template("update_patient.html",patient=pacientes)