from app.models import FriendRequest,Friend
from app import db
from datetime import datetime
from sqlalchemy import or_,and_

def Create(nguoinhan, nguoigui):
    friendRequest = FriendRequest(ReceiverId = nguoinhan, SenderId = nguoigui, CreatedAt = datetime.now())
    db.session.add(friendRequest)
    db.session.commit()
    return friendRequest

def GetAllByReceiverId(manguoinhan):
    return FriendRequest.query.filter(FriendRequest.ReceiverId == manguoinhan).order_by(FriendRequest.CreatedAt.desc()).all()

def GetAllBySenderId(manguoigui):
    return FriendRequest.query.filter(FriendRequest.SenderId == manguoigui).order_by(FriendRequest.CreatedAt.desc()).all()

def FindById(id):
    return FriendRequest.query.filter(FriendRequest.FriendRequestId == id).first_or_404()

def FindByClientId(client1,client2):
    
    return FriendRequest.query.filter(or_(and_(FriendRequest.SenderId == client1,FriendRequest.ReceiverId == client2),and_(FriendRequest.SenderId == client2, FriendRequest.ReceiverId==client1))).first_or_404()

def Delete(id):
    friendRequest = FriendRequest.get_id(id)
    db.session.delete(friendRequest)
    db.session.commit()
    return "Deleted"

def DeleteByClientId(receiverId,senderId):
    friendRequest = FriendRequest.query.filter(FriendRequest.SenderId == senderId,FriendRequest.ReceiverId == receiverId).first()
    db.session.delete(friendRequest)
    db.session.commit()
    return 'Deleted'

def Confirm(senderId,receiverId):
    friend1 = Friend(ClientId1 = senderId,ClientId2 = receiverId)
    friend2 = Friend(ClientId1 = receiverId, ClientId2 = senderId)
    db.session.add(friend1)
    db.session.add(friend2)
    db.session.commit()
    DeleteByClientId(senderId,receiverId)
    return 'Success'