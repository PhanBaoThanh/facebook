from app.models import Admin
from app import db
from datetime import datetime

def Create(username,password,name,dayOfBirth):
    if Admin.query.filter(Admin.Account == username).first():
        return None
    else:
        admin = Admin(Account=username,Password=password,Name=name,DateOfBirth=dayOfBirth)
        db.session.add(admin)
        db.session.commit()
        return admin
        

def Update(username,password,name,dayOfBirth):
    admin = Admin.query.filter(Admin.Account == username).first()
    admin.Password = password
    admin.Name = name
    admin.DateOfBirth = dayOfBirth
    db.session.commit()
    return admin

def Delete(id):
    admin = Admin.get_id(id)
    db.session.delete(admin)
    db.session.commit()
    return "Deleted"

def checkLogin(username, password):
    admin = Admin.query.filter_by(Account = username, Password = password).first_or_404()
    return admin
    