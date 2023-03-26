from app.models import Admin
from app import db

def Create(username,password,name,dayOfBirth):
    taikhoan = Admin.query.filter(Admin.TaiKhoan == username).first()
    if taikhoan:
        return None
    else:
        admin = Admin(TaiKhoan=username,MatKhau=password,HoTen=name,NgaySinh=dayOfBirth)
        db.session.add(admin)
        db.session.commit()

def Update(username,password,name,dayOfBirth):
    admin = Admin.query.filter(Admin.Username == username).first()
    admin.MatKhau = password
    admin.HoTen = name
    admin.NgaySinh = dayOfBirth
    db.session.commit()
    return admin

def Delete(id):
    admin = Admin.get_id(id)
    db.session.delete(admin)
    db.session.commit()
    return "Deleted"

def checkLogin(username, password):
    admin = Admin.query.filter_by(Admin.TaiKhoan == username, Admin.MatKhau == password).first_or_404()
    return admin
    