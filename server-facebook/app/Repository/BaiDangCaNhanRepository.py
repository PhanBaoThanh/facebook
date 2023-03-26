from app.models import BaiDangCaNhan
from app import db
from datetime import datetime

def Create(manguoidung, noidung, anh):
    baidangcanhan = BaiDangCaNhan(MaNguoiDung = manguoidung, ThoiGianDang = datetime.now(), NoiDung = noidung, Anh = anh)
    db.session.add(baidangcanhan)
    db.session.commit()
    return baidangcanhan

def Update(mabaidangcanhan, noidung, anh):
    baidangcanhan = BaiDangCaNhan.query.filter(BaiDangCaNhan.MaBaiDang == mabaidangcanhan).first()
    baidangcanhan.NoiDung = noidung
    baidangcanhan.Anh = anh
    baidangcanhan.ThoiGianDang = datetime.now()
    db.session.commit()
    return baidangcanhan

def GetAllByMaNguoiDung(manguoidung):
    return BaiDangCaNhan.query.filter(BaiDangCaNhan.MaNguoiDung == manguoidung).order_by(BaiDangCaNhan.ThoiGianDang.desc()).all()

def FindById(id):
    return BaiDangCaNhan.query.filter(BaiDangCaNhan.MaBaiDang == id).first_or_404()

def FindByKey(key):
    return BaiDangCaNhan.query.filter(BaiDangCaNhan.NoiDung.like('%' +key+'%')).all()

def Delete(id):
    baidangcanhan = BaiDangCaNhan.get_id(id)
    db.session.delete(baidangcanhan)
    db.session.commit()
    return "Deleted"