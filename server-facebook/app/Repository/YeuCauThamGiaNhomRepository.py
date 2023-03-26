from app.models import YeuCauThamGiaNhom
from app import db
from datetime import datetime

def Create(manhom, manguoidung):
    yeucauthamgianhom = YeuCauThamGiaNhom(MaNhom = manhom, MaNguoiDung = manguoidung, ThoiGianGui = datetime.now())
    db.session.add(yeucauthamgianhom)
    db.session.commit()
    return yeucauthamgianhom

def GetAllByMaNguoiDung(manguoidung):
    return YeuCauThamGiaNhom.query.filter(YeuCauThamGiaNhom.MaNguoiDung == manguoidung).order_by(YeuCauThamGiaNhom.ThoiGianGui.desc()).all()

def GetAllByMaNhom(manhom):
    return YeuCauThamGiaNhom.query.filter(YeuCauThamGiaNhom.MaNhom == manhom).order_by(YeuCauThamGiaNhom.ThoiGianGui.desc()).all()

def FindById(id):
    return YeuCauThamGiaNhom.query.filter(YeuCauThamGiaNhom.MaYeuCauThamGiaNhom == id).first_or_404()

def Delete(id):
    yeucauthamgianhom = YeuCauThamGiaNhom.get_id(id)
    db.session.delete(yeucauthamgianhom)
    db.session.commit()
    return "Deleted"