from app.models import Group
from app import db
from datetime import datetime

def Create(tenGroup,anhbia,riengtu):
    group = Group( Name = tenGroup,CreatedAt = datetime.now()  , BackgroundImg = anhbia, IsPrivate = riengtu)
    db.session.add(group)
    db.session.commit()
    return group

def Update(maGroup,tenGroup,riengtu):
    group = Group.query.filter(Group.GroupId == maGroup).first()
    group.Name = tenGroup
    group.IsPrivate = riengtu
    db.session.commit()
    return group

def Delete(id):
    group = Group.query.filter(Group.GroupId == id).first()
    db.session.delete(group)
    db.session.commit()
    return "Deleted"

def UpdateBackgroundImage(maGroup,backgroundImg):
    group = Group.query.filter(Group.GroupId == maGroup).first()
    group.BackgroundImg = backgroundImg
    db.session.commit()
    return group

def findById(id):
    return Group.query.filter(Group.GroupId == id).first_or_404()

def Search(key):
    return Group.query.filter(Group.Name.like('%'+key+'%')).all()