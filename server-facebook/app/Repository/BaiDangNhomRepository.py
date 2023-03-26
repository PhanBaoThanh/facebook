from app.models import BaiDangNhom
from app import db
from datetime import datetime

def Create(manhom,manguoidung,  noidung, anh):
    baidangnhom = BaiDangNhom(MaNhom = manhom, MaNguoiDung = manguoidung, ThoiGianDang = datetime.now(), NoiDung = noidung, Anh = anh)
    db.session.add(baidangnhom)
    db.session.commit()
    return baidangnhom

def Update(mabaidangnhom, noidung, anh):
    baidangnhom = BaiDangNhom.query.filter(BaiDangNhom.MaBaiDang == mabaidangnhom).first()
    baidangnhom.NoiDung = noidung
    baidangnhom.Anh = anh
    baidangnhom.ThoiGianDang = datetime.now()
    db.session.commit()
    return baidangnhom

def GetAllByMaNhom(manhom):
    return BaiDangNhom.query.filter(BaiDangNhom.MaNhom == manhom).order_by(BaiDangNhom.ThoiGianDang.desc()).all()

def FindById(id):
    return BaiDangNhom.query.filter(BaiDangNhom.MaBaiDang == id).first_or_404()

def FindByKey(key):
    return BaiDangNhom.query.filter(BaiDangNhom.NoiDung.like('%' + key + '%')).order_by(BaiDangNhom.ThoiGianDang.desc()).all()

def FindByMaNguoiDung(manhom, manguoidung):
    return BaiDangNhom.query.filter(BaiDangNhom.MaNhom == manhom and BaiDangNhom.MaNguoiDung == manguoidung).order_by(BaiDangNhom.ThoiGianDang.desc()).all()

def Delete(id):
    baidangnhom = BaiDangNhom.get_id(id)
    db.session.delete(baidangnhom)
    db.session.commit()
    return "Deleted"