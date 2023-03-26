from app.models import PostConfirm,Post
from app import db
from datetime import datetime


def Create(manhom, manguoidung, noidung, anh):
    postConfirm = PostConfirm(GroupId = manhom, ClientId = manguoidung, CreatedAt = datetime.now(), Content = noidung, Img = anh)
    db.session.add(postConfirm)
    db.session.commit()
    return postConfirm

def GetAllByGroupId(manhom):
    return PostConfirm.query.filter(PostConfirm.GroupId == manhom).order_by(PostConfirm.CreatedAt.desc()).all()

def FindById(id):
    return PostConfirm.query.filter(PostConfirm.PostConfirmId == id).first_or_404()

def Delete(id):
    postConfirm = PostConfirm.get_id(id)
    db.session.delete(postConfirm)
    db.session.commit()
    return "Deleted"

def Confirm(id):
    postConfirm = PostConfirm.query.filter(PostConfirm.PostConfirmId == id).first()
    post = Post(GroupId = postConfirm.GroupId, ClientId = postConfirm.ClientId, CreatedAt = datetime.now(), Content = postConfirm.Content, Img = postConfirm.Img)
    db.session.add(post)    
    db.session.delete(postConfirm)
    db.session.commit()
    return 'Success'