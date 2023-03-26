from app.models import YeuCauKetBan
from app import db
from datetime import datetime

def Create(nguoinhan, nguoigui):
    yeucauketban = YeuCauKetBan(MaNguoiNhan = nguoinhan, MaNguoiGui = nguoigui, ThoiGianGui = datetime.now())
    db.session.add(yeucauketban)
    db.session.commit()
    return yeucauketban

def GetAllByMaNguoiNhan(manguoinhan):
    return YeuCauKetBan.query.filter(YeuCauKetBan.MaNguoiNhan == manguoinhan).order_by(YeuCauKetBan.ThoiGianGui.desc()).all()

def GetAllByMaNguoiGui(manguoigui):
    return YeuCauKetBan.query.filter(YeuCauKetBan.MaNguoiGui == manguoigui).order_by(YeuCauKetBan.ThoiGianGui.desc()).all()

def FindById(id):
    return YeuCauKetBan.query.filter(YeuCauKetBan.MaYeuCauKetBan == id).first_or_404()

def Delete(id):
    yeucauketban = YeuCauKetBan.get_id(id)
    db.session.delete(yeucauketban)
    db.session.commit()
    return "Deleted"