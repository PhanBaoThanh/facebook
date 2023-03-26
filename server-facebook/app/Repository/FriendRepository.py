from app.models import Friend
from app import db

def Create(manguoidung1,manguoidung2):
    friend = Friend(manguoidung1, manguoidung2)
    db.session.add(friend)
    db.session.commit()
    return friend

def FindById(id):
    return Friend.query.filter(Friend.MaBan == id).first_or_404()

def FindAllByMaNguoiDung(manguoidung):
    return Friend.query.filter(Friend.MaNguoiDung1 == manguoidung or Friend.MaNguoiDung2 == manguoidung).all()

def Delete(id):
    friend = Friend.get_id(id)
    db.session.delete(friend)
    db.session.commit()
    return "Deleted"