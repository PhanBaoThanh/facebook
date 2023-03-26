from app.models import CamXucBaiDangNhom
from app import db

def Create(manhom, mabaidang, manguoidung):
    camxucbaidangnhom = CamXucBaiDangNhom(MaNhom = manhom, MaBaiDang = mabaidang, MaNguoiDung = manguoidung)
    db.session.add(camxucbaidangnhom)
    db.session.commit()
    return camxucbaidangnhom

def GetCountByMaBaiDang(manhom,mabaidang):
    return CamXucBaiDangNhom.query.filter(CamXucBaiDangNhom.MaBaiDang == mabaidang and CamXucBaiDangNhom.MaNhom == manhom).count()

def GetAllByMaBaiDang(mabaidang):
    return CamXucBaiDangNhom.query.filter(CamXucBaiDangNhom.MaBaiDang == mabaidang).all()

def GetAllByMaNguoiDung(manguoidung):
    return CamXucBaiDangNhom.query.filter(CamXucBaiDangNhom.MaNguoiDung == manguoidung).all()

def FindById(id):
    return CamXucBaiDangNhom.query.filter(CamXucBaiDangNhom.MaCamXuc == id).first_or_404()

def Delete(id):
    camxucbaidangnhom = CamXucBaiDangNhom.get_id(id)
    db.session.delete(camxucbaidangnhom)
    db.session.commit()
    return "Deleted"