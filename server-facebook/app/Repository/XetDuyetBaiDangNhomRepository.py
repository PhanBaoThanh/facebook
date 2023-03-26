from app.models import XetDuyetBaiDangNhom,BaiDangNhom
from app import db
from datetime import datetime

def Create(manhom, manguoidung, noidung, anh):
    xetduyetbaidangnhom = XetDuyetBaiDangNhom(MaNhom = manhom, MaNguoiDung = manguoidung, ThoiGianDang = datetime.now(), NoiDung = noidung, Anh = anh)
    db.session.add(xetduyetbaidangnhom)
    db.session.commit()
    return xetduyetbaidangnhom

def GetAllByMaNhom(manhom):
    return XetDuyetBaiDangNhom.query.filter(XetDuyetBaiDangNhom.MaNhom == manhom).order_by(XetDuyetBaiDangNhom.ThoiGianDang.desc()).all()

def FindById(id):
    return XetDuyetBaiDangNhom.query.filter(XetDuyetBaiDangNhom.MaXetDuyet == id).first_or_404()

def Delete(id):
    xetduyetbaidangnhom = XetDuyetBaiDangNhom.get_id(id)
    db.session.delete(xetduyetbaidangnhom)
    db.session.commit()
    return "Deleted"

def Confirm(id):
    xetduyet = XetDuyetBaiDangNhom.query.filter(MaXetDuyet == id)
    xetduyetbaidangnhom = XetDuyetBaiDangNhom.get_id(id)
    baidangnhom = BaiDangNhom(MaNhom = xetduyet.MaNhom, MaNguoiDung = xetduyet.MaNguoiDung, ThoiGianDang = datetime.now(), NoiDung = xetduyet.NoiDung, Anh = xetduyet.Anh)
    db.session.add(baidangnhom)    
    db.session.delete(xetduyetbaidangnhom)
    db.session.commit()
    return 'Success'