from app.models import Friend
from app import db
from sqlalchemy import or_

def Create(manguoidung1,manguoidung2):
    friend1 = Friend(ClientId1 = manguoidung1,ClientId2 = manguoidung2)
    friend2 = Friend(ClientId1 = manguoidung2, ClientId2 = manguoidung1)
    db.session.add(friend1)
    db.session.add(friend2)
    db.session.commit()
    return friend1

def FindFriendByClientId(client1,client2):
    return Friend.query.filter(Friend.ClientId1 == client1,Friend.ClientId2==client2).first_or_404()

def FindById(id):
    return Friend.query.filter(Friend.FriendId == id).first_or_404()

def Delete(client1,client2):
    friend1 = Friend.query.filter(Friend.ClientId1 == client1,Friend.ClientId2==client2).first()
    friend2 = Friend.query.filter(Friend.ClientId1 == client2,Friend.ClientId2==client1).first()
    db.session.delete(friend1)
    db.session.delete(friend2)
    db.session.commit()
    return "Deleted"