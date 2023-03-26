from app.Repository import NhomRepository

def createNhom(maquantrivien,tennhom,anh,anhbia,riengtu):
    return NhomRepository.Create(maquantrivien,tennhom,anh,anhbia,riengtu)

def updateNhom(manhom,tennhom,riengtu):
    return NhomRepository.Update(manhom,tennhom,riengtu)

def deleteNhom(id):
    return NhomRepository.Delete(id)

def updateAvatar(manhom,avt):
    return NhomRepository.UpdateAvatar(manhom,avt)

def updateBackgroundImage(manhom,backgroundImg):
    return NhomRepository.UpdateBackgroundImage(manhom,backgroundImg)

def findNhomById(id):
    return NhomRepository.findById(id)

def searchNhom(key):
    return NhomRepository.Search(key)