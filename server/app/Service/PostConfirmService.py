from app.Repository import PostConfirmRepository

def createPostConfirm(manhom,manguoidung,noidung,anh):
    return PostConfirmRepository.Create(manhom,manguoidung,noidung,anh)

def getAllPostConfirmByGroupId(manhom):
    return PostConfirmRepository.GetAllByGroupId(manhom)

def finedPostConfirmById(id):
    return PostConfirmRepository.FindById(id)

def deletedPostConfirm(id):
    return PostConfirmRepository.Delete(id)

def confirmed(id):
    return PostConfirmRepository.Confirm(id)