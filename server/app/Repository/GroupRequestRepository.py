from app.models import GroupRequest,GroupMember
from app import db
from datetime import datetime
from sqlalchemy import and_

def Create(manhom, manguoidung):
    groupRequest = GroupRequest(GroupId = manhom, ClientId = manguoidung, CreatedAt = datetime.now())
    db.session.add(groupRequest)
    db.session.commit()
    return groupRequest

def GetAllByClientId(manguoidung):
    return GroupRequest.query.filter(GroupRequest.ClientId == manguoidung).order_by(GroupRequest.CreatedAt.desc()).all()

def GetAllByGroupId(manhom):
    return GroupRequest.query.filter(GroupRequest.GroupId == manhom).order_by(GroupRequest.CreatedAt.desc()).all()

def FindById(id):
    return GroupRequest.query.filter(GroupRequest.GroupRequestId == id).first_or_404()

def FindByClientIdAndGroupId(clientId,groupId):
    return GroupRequest.query.filter(GroupRequest.ClientId == clientId,GroupRequest.GroupId == groupId).first_or_404()

def Delete(id):
    groupRequest = GroupRequest.get_id(id)
    db.session.delete(groupRequest)
    db.session.commit()
    return "Deleted"

def DeleteByClientIdAndGroupId(clientId,groupId):
    groupRequest = GroupRequest.query.filter(GroupRequest.ClientId == clientId,GroupRequest.GroupId == groupId).first()
    db.session.delete(groupRequest)
    db.session.commit()
    return 'Deleted'

def Confirm(id):
    groupRequest = GroupRequest.query.filter(GroupRequest.GroupRequestId == id).first()
    groupMember = GroupMember(GroupId = groupRequest.GroupId, ClientId = groupRequest.ClientId)
    db.session.add(groupMember)
    db.session.delete(groupRequest)
    db.session.commit()
    return 'Success'

def ConfirmByClientIdAndGroupId(clientId,groupId):
    member = GroupMember(GroupId = groupId, ClientId = clientId)
    groupRequestItem = GroupRequest.query.filter(GroupRequest.ClientId == clientId,GroupRequest.GroupId == groupId).first()
    db.session.add(member)
    db.session.delete(groupRequestItem)
    db.session.commit()
    return 'Confirmed'