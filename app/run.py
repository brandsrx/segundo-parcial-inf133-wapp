from flask import Flask
from flask_login import LoginManager
from controllers.paciente_controller import pac_bp
from controllers.usuarios_controllers import user_bp
from database import db
from models.usuarios_models import Usuarios
from models.pacientes_models import Pacientes
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///CNS.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]="clave-secreta"

login_manager = LoginManager()

login_manager.login_view = "user.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))    

db.init_app(app)

app.register_blueprint(pac_bp)
app.register_blueprint(user_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
