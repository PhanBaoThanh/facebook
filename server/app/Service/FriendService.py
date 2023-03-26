from app.Repository import FriendRepository

def createFriend(manguoidung1,manguoidung2):
    return FriendRepository.Create(manguoidung1,manguoidung2)

def findFriendById(id):
    return FriendRepository.FindById(id)

def FindFriendByClientId(client1,client2):
    return FriendRepository.FindFriendByClientId(client1,client2)

def deleteFriend(client1,client2):
    return FriendRepository.Delete(client1,client2)