from app.Repository import FriendRepository

def createFriend(manguoidung1,manguoidung2):
    return FriendRepository.Create(manguoidung1,manguoidung2)

def findFriendById(id):
    return FriendRepository.FindById(id)

def findFriendByMaNguoiDung(manguoidung):
    return FriendRepository.FindAllByMaNguoiDung(manguoidung)

def deleteFriend(id):
    return FriendRepository.Delete(id)