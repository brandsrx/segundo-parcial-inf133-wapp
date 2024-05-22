from flask import redirect,url_for,Blueprint,request,flash
from flask_login import login_required,current_user,login_user,logout_user
from werkzeug.security import check_password_hash
from models.usuarios_models import Usuarios
from views import users_view

user_bp = Blueprint("user",__name__)

@user_bp.route("/",methods=["GET"])
def index():
    return redirect(url_for("user.login"))

@user_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = Usuarios.find_by_username(username)
        
        if user and check_password_hash(user.password_hash,password):
            login_user(user)
            flash("Inicio de sesion exitoso","success")
            return redirect(url_for("paciente.list_pacientes"))
        
    return users_view.login()

@user_bp.route("/users", methods=["GET","POST"])
def create_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        roles = request.form["role"]

        existing_user = Usuarios.find_by_username(username)
        if existing_user:
            flash("El nombre de usuario no disponible","error")
            return  redirect(url_for("user.create_user"))
        else:
            new_user = Usuarios(username, password, roles)
            new_user.set_password(password)
            new_user.save()
            flash("usuario creado exitosamente","success")
            return redirect(url_for("paciente.list_pacientes"))
    return users_view.register()

@user_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("user.index"))