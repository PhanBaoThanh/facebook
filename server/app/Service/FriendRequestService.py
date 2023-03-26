from app.Repository import FriendRequestRepository

def createFriendRequest(nguoinhan,nguoigui):
    return FriendRequestRepository.Create(nguoinhan,nguoigui)

def getAllFriendRequestByReceiverId(manguoinhan):
    return FriendRequestRepository.GetAllByReceiverId(manguoinhan)

def getAllFriendRequestBySenderId(manguoigui):
    return FriendRequestRepository.GetAllBySenderId(manguoigui)

def findFriendRequestById(id):
    return FriendRequestRepository.FindById(id)

def findFriendRequestByClientId(client1,client2):
    return FriendRequestRepository.FindByClientId(client1,client2)

def confirmFriendRequest(receiverId,senderId):
    return FriendRequestRepository.Confirm(receiverId,senderId)

def deleteFriendRequest(id):
    return FriendRequestRepository.Delete(id)

def deleteFriendRequestByClientId(receiverId,senderId):
    return FriendRequestRepository.DeleteByClientId(receiverId,senderId)

