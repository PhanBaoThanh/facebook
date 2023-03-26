from app.Repository import PostRepository

def createPost(manhom,manguoidung,noidung,anh):
    return PostRepository.Create(manhom,manguoidung,noidung,anh)

def updatePost(mabaidangnhom, noidung, anh):
    return PostRepository.Update(mabaidangnhom,noidung,anh)

def findPostById(id):
    return PostRepository.FindById(id)

def findPostByKey(key):
    return PostRepository.Search(key)

def getAllPostOfGroup(manhom):
    return PostRepository.GetAllOfGroup(manhom)

def getAllPostByClientIdAndGroupId(manhom,manguoidung):
    return PostRepository.GetAllByClientIdAndGroupId(manhom,manguoidung)

def getAllPostOfFriend(clientId):
    return PostRepository.GetAllPostOfFriend(clientId)

def getAllPostOfClient(clientId):
    return PostRepository.GetAllOfClient(clientId)

def deletePost(id):
    return PostRepository.Delete(id)