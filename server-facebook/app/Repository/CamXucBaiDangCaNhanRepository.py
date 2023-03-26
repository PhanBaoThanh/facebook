from app.models import CamXucBaiDangCaNhan
from app import db

def Create(mabaidang, manguoidung):
    camxucbaidangcanhan = CamXucBaiDangCaNhan(MaBaiDang = mabaidang, MaNguoidDung = manguoidung)
    db.session.add(camxucbaidangcanhan)
    db.session.commit()
    return camxucbaidangcanhan

def GetCountByMaBaiDang(mabaidang):
    return CamXucBaiDangCaNhan.query.filter(CamXucBaiDangCaNhan.MaBaiDang == mabaidang).count()

def GetAllByMaBaiDang(mabaidang):
    return CamXucBaiDangCaNhan.query.filter(CamXucBaiDangCaNhan.MaBaiDang == mabaidang).all()

def GetAllByMaNguoiDung(manguoidung):
    return CamXucBaiDangCaNhan.query.filter(CamXucBaiDangCaNhan.MaNguoiDung == manguoidung).all()

def FindById(id):
    return CamXucBaiDangCaNhan.query.filter(CamXucBaiDangCaNhan.MaCamXuc == id).first_or_404()

def Delete(id):
    camxucbaidangcanhan = CamXucBaiDangCaNhan.get_id(id)
    db.session.delete(camxucbaidangcanhan)
    db.session.commit()
    return "Deleted"