from app.models import NguoiDung
from app import db

def Create(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia):
    if NguoiDung.query.filter(NguoiDung.TaiKhoan == taikhoan).first():
        return None
    else:
        nguoidung = NguoiDung(HoTen = hoten, SDT = sdt, Email = email, TaiKhoan = taikhoan, MatKhau= matkhau, GioiTinh=gioitinh, NgaySinh = ngaysinh, Anh=anh, AnhBia = anhbia)
        db.session.add(nguoidung)
        db.session.commit()
        return nguoidung

def Update(hoten,sdt,email,taikhoan,gioitinh,ngaysinh):
    nguoidung = NguoiDung.query.filter(NguoiDung.TaiKhoan == taikhoan).first()
    nguoidung.HoTen = hoten
    nguoidung.NgaySinh = ngaysinh
    nguoidung.Email = email
    nguoidung.SDT = sdt
    nguoidung.GioiTinh = gioitinh
    db.session.commit()
    return nguoidung

def Delete(id):
    nguoidung = NguoiDung.get_id(id)
    db.session.delete(nguoidung)
    db.session.commit()
    return "Deleted"

def UpdatePassword(taikhoan,matkhau):
    nguoidung = NguoiDung.query.filter(NguoiDung.TaiKhoan == taikhoan).first()
    nguoidung.MatKhau = matkhau
    db.session.commit()
    return nguoidung

def UpdateAvatar(taikhoan,avt):
    nguoidung = NguoiDung.query.filter(NguoiDung.TaiKhoan == taikhoan).first()
    nguoidung.Anh = avt
    db.session.commit()
    return nguoidung

def UpdateBackgroundImage(taikhoan,backgroundImg):
    nguoidung = NguoiDung.query.filter(NguoiDung.TaiKhoan == taikhoan).first()
    nguoidung.AnhBia = backgroundImg
    db.session.commit()
    return nguoidung

def findById(id):
    return NguoiDung.query.filter(NguoiDung.MaNguoiDung == id).first_or_404()

def Search(key):
    return NguoiDung.query.filter(NguoiDung.HoTen.like('%'+key+'%')).all()

def checkLogin(taikhoan, matkhau):
    nguoidung = NguoiDung.query.filter_by(TaiKhoan = taikhoan, MatKhau = matkhau).first_or_404()
    return nguoidung