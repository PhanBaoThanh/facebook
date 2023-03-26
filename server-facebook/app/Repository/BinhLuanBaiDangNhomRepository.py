from app.models import BinhLuanBaiDangNhom
from app import db
from datetime import datetime

def Create(manhom, mabaidang, manguoidung , noidung):
    binhluanbaidangnhom = BinhLuanBaiDangNhom(MaNhom = manhom, MaBaiDang = mabaidang, MaNguoidDung = manguoidung, NoiDung = noidung, ThoiGian = datetime.now())
    db.session.add(binhluanbaidangnhom)
    db.session.commit()
    return binhluanbaidangnhom

def Update(mabinhluanbaidangnhom, noidung):
    binhluanbaidangnhom = BinhLuanBaiDangNhom.query.filter(BinhLuanBaiDangNhom.MaBinhLuan == mabinhluanbaidangnhom).first()
    binhluanbaidangnhom.NoiDung = noidung
    binhluanbaidangnhom.ThoiGian = datetime.now()
    db.session.commit()
    return binhluanbaidangnhom

def GetAllByMaBaiDang(mabaidang, manhom):
    return BinhLuanBaiDangNhom.query.filter(BinhLuanBaiDangNhom.MaBaiDang == mabaidang and BinhLuanBaiDangNhom.MaNhom == manhom).order_by(BinhLuanBaiDangNhom.ThoiGian.desc()).all()

def FindById(id):
    return BinhLuanBaiDangNhom.query.filter(BinhLuanBaiDangNhom.MaBinhLuan == id).first_or_404()

def Delete(id):
    binhluanbaidangnhom = BinhLuanBaiDangNhom.get_id(id)
    db.session.delete(binhluanbaidangnhom)
    db.session.commit()
    return "Deleted"