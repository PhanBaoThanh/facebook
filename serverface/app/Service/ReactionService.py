from app.Repository import ReactionRepository

def createReaction(mabaidang,manguoidung):
    return ReactionRepository.Create(mabaidang,manguoidung)

def getCountByPostId(mabaidang):
    return ReactionRepository.GetCountByPostId(mabaidang)

def getAllReactionByPostId(mabaidang):
    return ReactionRepository.GetAllByPostId(mabaidang)

def getAllReactionByClientId(manguoidung):
    return ReactionRepository.GetAllByClientId(manguoidung)

def findReactionById(id):
    return ReactionRepository.FindById(id)

def deleteReaction(id):
    return ReactionRepository.Delete(id)

def deleteReactionByClientIdAndPostId(clientId,postId):
    return ReactionRepository.DeleteByClientIdAndPostId(clientId,postId)