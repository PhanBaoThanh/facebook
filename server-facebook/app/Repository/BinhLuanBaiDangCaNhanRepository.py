from app.models import BinhLuanBaiDangCaNhan
from app import db
from datetime import datetime

def Create(mabaidang, manguoidung , noidung):
    binhluanbaidangcanhan = BinhLuanBaiDangCaNhan(MaBaiDang = mabaidang, MaNguoidDung = manguoidung, NoiDung = noidung, ThoiGian = datetime.now())
    db.session.add(binhluanbaidangcanhan)
    db.session.commit()
    return binhluanbaidangcanhan

def Update(mabinhluanbaidangcanhan, noidung):
    binhluanbaidangcanhan = BinhLuanBaiDangCaNhan.query.filter(BinhLuanBaiDangCaNhan.MaBinhLuan == mabinhluanbaidangcanhan).first()
    binhluanbaidangcanhan.NoiDung = noidung
    binhluanbaidangcanhan.ThoiGian = datetime.now()
    db.session.commit()
    return binhluanbaidangcanhan

def GetAllByMaBaiDang(mabaidang):
    return BinhLuanBaiDangCaNhan.query.filter(BinhLuanBaiDangCaNhan.MaBaiDang == mabaidang).order_by(BinhLuanBaiDangCaNhan.ThoiGian.desc()).all()

def FindById(id):
    return BinhLuanBaiDangCaNhan.query.filter(BinhLuanBaiDangCaNhan.MaBinhLuan == id).first_or_404()

def Delete(id):
    binhluanbaidangcanhan = BinhLuanBaiDangCaNhan.get_id(id)
    db.session.delete(binhluanbaidangcanhan)
    db.session.commit()
    return "Deleted"