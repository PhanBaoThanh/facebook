from app.models import ThanhVienNhom
from app import db

def Create(manhom,manguoidung):
    thanhviennhom = ThanhVienNhom(MaNhom = manhom, MaNguoiDung = manguoidung)
    db.session.add(thanhviennhom)
    db.session.commit()
    return thanhviennhom

def GetAllByMaNhom(manhom):
    return ThanhVienNhom.query.filter(ThanhVienNhom.MaNhom == manhom).all()

def FindById(id):
    return ThanhVienNhom.query.filter(ThanhVienNhom.MaThanhVienNhom == id).first_or_404()

def FindAllByMaNguoiDung(manguoidung):
    return ThanhVienNhom.query.filter(ThanhVienNhom.MaNguoiDung == manguoidung).all()

def Delete(id):
    thanhviennhom = ThanhVienNhom.get_id(id)
    db.session.delete(thanhviennhom)
    db.session.commit()
    return "Deleted"