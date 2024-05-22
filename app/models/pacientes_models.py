from database import db

class Pacientes(db.Model):
    __tablename___ = "pacientes"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=True)
    lastname = db.Column(db.String,nullable=True)
    ci = db.Column(db.String,nullable=True)
    date = db.Column(db.Date,nullable=True)
    
    def __init__(self,name,lastname,ci,date):
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.date = date
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_all():
        return Pacientes.query.all()
    @staticmethod
    def get_by_id(id):
        return Pacientes.query.get(id)
    
    def update(self, name=None, lastname=None, ci=None,date=None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if date is not None:
            self.date = date
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()