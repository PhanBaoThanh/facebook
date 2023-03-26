from app.models import Nhom
from app import db

def Create(maquantrivien,tennhom,anh,anhbia,riengtu):
    nhom = Nhom(MaQuanTriVien = maquantrivien, TenNhom = tennhom, Anh = anh, AnhBia = anhbia, RiengTu = riengtu)
    db.session.add(nhom)
    db.session.commit()
    return nhom

def Update(manhom,tennhom,riengtu):
    nhom = Nhom.query.filter(Nhom.MaNhom == manhom).first()
    nhom.TenNhom = tennhom
    nhom.RiengTu = riengtu
    db.session.commit()
    return nhom

def Delete(id):
    nhom = Nhom.get_id(id)
    db.session.delete(nhom)
    db.session.commit()
    return "Deleted"

def UpdateAvatar(manhom,avt):
    nhom = Nhom.query.filter(Nhom.MaNhom == manhom).first()
    nhom.Anh = avt
    db.session.commit()
    return nhom

def UpdateBackgroundImage(manhom,backgroundImg):
    nhom = Nhom.query.filter(Nhom.MaNhom == manhom).first()
    nhom.AnhBia = backgroundImg
    db.session.commit()
    return nhom

def findById(id):
    return Nhom.query.filter(Nhom.MaNhom == id).first_or_404()

def Search(key):
    return Nhom.query.filter(Nhom.TenNhom.like('%'+key+'%')).all()