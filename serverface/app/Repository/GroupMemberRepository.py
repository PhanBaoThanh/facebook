from app.models import GroupMember
from app import db
from sqlalchemy import and_

def Create(manhom,manguoidung,isAdmin):
    groupMember = GroupMember(GroupId = manhom, ClientId = manguoidung,IsAdmin = isAdmin)
    db.session.add(groupMember)
    db.session.commit()
    return groupMember

def Update(manhom,manguoidung,isAdmin):
    groupMember = GroupMember.query.filter(GroupMember.GroupId == manhom, GroupMember.ClientId == manguoidung).first()
    groupMember.IsAdmin = isAdmin
    db.session.commit()
    return groupMember

def FindGroupMemberByClientIdAndGroupId(clientId,groupId):
    return GroupMember.query.filter(GroupMember.GroupId == groupId,GroupMember.ClientId == clientId).first_or_404()

def GetAllByGroupId(manhom):
    return GroupMember.query.filter(GroupMember.GroupId == manhom).all()

def FindById(id):
    return GroupMember.query.filter(GroupMember.GroupMemberId == id).first_or_404()

def GetAllByClientId(manguoidung):
    return GroupMember.query.filter(GroupMember.ClientId == manguoidung).all()

def Delete(id):
    groupMember = GroupMember.query.filter(GroupMember.GroupMemberId == id).first()
    db.session.delete(groupMember)
    db.session.commit()
    return "Deleted"

def DeleteByClientIdAndGroupId(clientId,groupId):
    groupMember = GroupMember.query.filter(GroupMember.GroupId == groupId, GroupMember.ClientId == clientId).first()
    db.session.delete(groupMember)
    db.session.commit()
    return 'Deleted'

def DeleteAndUpdateNewAdmin(clientId,groupId,adminId):
    client = GroupMember.query.filter(GroupMember.ClientId == clientId,GroupMember.GroupId == groupId).first()
    admin = GroupMember.query.filter(GroupMember.ClientId == adminId, GroupMember.GroupId == groupId).first()
    admin.IsAdmin = True
    db.session.delete(client)
    db.session.commit()
    return 'Deleted'
    