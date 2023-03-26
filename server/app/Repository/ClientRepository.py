from app.models import Client
from app import db

def Create(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia):
    if Client.query.filter(Client.Account == taikhoan).first():
        return None
    else:
        client = Client(Name = hoten, PhoneNumber = sdt, Email = email, Account = taikhoan, Password= matkhau, Sex=gioitinh, DayOfBirth = ngaysinh, Avatar=anh, BackgroundImg = anhbia)
        db.session.add(client)
        db.session.commit()
        return client

def Update(clientId,hoten,sdt,email,gioitinh,ngaysinh):
    client = Client.query.filter(Client.ClientId == clientId).first()
    client.Name = hoten
    client.DayOfBirth = ngaysinh
    client.Email = email
    client.PhoneNumber = sdt
    client.Sex = gioitinh
    db.session.commit()
    return client

def Delete(id):
    client = Client.get_id(id)
    db.session.delete(client)
    db.session.commit()
    return "Deleted"

def UpdatePassword(clientId,matkhaucu,matkhaumoi):
    client = Client.query.filter(Client.ClientId == clientId,Client.Password == matkhaucu).first()
    client.Password = matkhaumoi
    db.session.commit()
    return client

def UpdateAvatar(clientId,avt):
    client = Client.query.filter(Client.ClientId == clientId).first()
    client.Avatar = avt
    db.session.commit()
    return client

def UpdateBackgroundImage(clientId,backgroundImg):
    client = Client.query.filter(Client.ClientId == clientId).first()
    client.BackgroundImg = backgroundImg
    db.session.commit()
    return client

def findById(clientId):
    return Client.query.filter(Client.ClientId == clientId).first_or_404()

def Search(key,clientId):
    return Client.query.filter(Client.Name.like('%'+key+'%'),Client.ClientId != clientId).all()

def checkLogin(taikhoan, matkhau):
    client = Client.query.filter_by(Account = taikhoan, Password = matkhau).first_or_404()
    return client