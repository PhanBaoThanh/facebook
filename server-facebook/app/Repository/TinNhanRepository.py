from app.models import TinNhan
from app import db
from datetime import datetime

def Create(nguoigui,nguoinhan,noidung):
    tinnhan = TinNhan(MaNguoiGui = nguoigui, MaNguoiNhan = nguoinhan, NoiDung = noidung, ThoiGianGui = datetime.now())
    db.session.add(tinnhan)
    db.session.commit()
    return tinnhan

def GetAllByMaNguoiDung(nguoidung1, nguoidung2):
    return TinNhan.query.filter((TinNhan.MaNguoiGui == nguoidung1 and TinNhan.MaNguoiNhan == nguoidung2) or (TinNhan.MaNguoiGui == nguoidung2 and TinNhan.MaNguoiNhan == nguoidung1)).order_by(TinNhan.ThoiGianGui.asc()).all()

def FindById(id):
    return TinNhan.query.filter(TinNhan.MaTinNhan == id).first_or_404()

def Delete(id):
    tinnhan = TinNhan.get_id(id)
    db.session.delete(tinnhan)
    db.session.commit()
    return "Deleted"