from app.Repository import TinNhanRepository

def createTinNhan(nguoigui,nguoinhan,noidung):
    return TinNhanRepository.Create(nguoigui,nguoinhan,noidung)

def getAllTinNhanByMaNguoiDung(nguoidung1,nguoidung2):
    return TinNhanRepository.GetAllByMaNguoiDung(nguoidung1,nguoidung2)

def findTinNhanById(id):
    return TinNhanRepository.FindById(id)

def deleteTinNhan(id):
    return TinNhanRepository.Delete(id)