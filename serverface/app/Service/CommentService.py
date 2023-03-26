from app.Repository import CommentRepository

def createComment(mabaidang,manguoidung,noidung):
    return CommentRepository.Create(mabaidang,manguoidung,noidung)

def updateComment(mabinhluan,noidung):
    return CommentRepository.Update(maComment= mabinhluan,noidung = noidung)

def getAllCommentByPostId(mabaidang):
    return CommentRepository.GetAllByPostId(mabaidang)

def findCommentById(id):
    return CommentRepository.FindById(id)

def deleteComment(id):
    return CommentRepository.Delete(id)