from app.Repository import CamXucBaiDangCaNhanRepository

def createCamXucBaiDangCaNhan(mabaidang,manguoidung):
    return CamXucBaiDangCaNhanRepository.Create(mabaidang,manguoidung)

def getCountByMaBaiDang(mabaidang):
    return CamXucBaiDangCaNhanRepository.GetCountByMaBaiDang(mabaidang)

def getAllCamXucBaiDangCaNhanByMaBaiDang(mabaidang):
    return CamXucBaiDangCaNhanRepository.GetAllByMaBaiDang(mabaidang)

def getAllCamXucBaiDangCaNhanByMaNguoiDung(manguoidung):
    return CamXucBaiDangCaNhanRepository.GetAllByMaNguoiDung(manguoidung)

def findCamXucBaiDangCaNhanById(id):
    return CamXucBaiDangCaNhanRepository.FindById(id)

def deleteCamXucBaiDangCaNhan(id):
    return CamXucBaiDangCaNhanRepository.Delete(id)