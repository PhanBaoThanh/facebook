from app.Repository import CamXucBaiDangNhomRepository

def createCamXucBaiDangNhom(manhom,mabaidang,manguoidung):
    return CamXucBaiDangNhomRepository.Create(manhom,mabaidang,manguoidung)

def getCountByMaBaiDang(manhom,mabaidang):
    return CamXucBaiDangNhomRepository.GetCountByMaBaiDang(manhom,mabaidang)

def getAllCamXucBaiDangNhomByMaBaiDang(mabaidang):
    return CamXucBaiDangNhomRepository.GetAllByMaBaiDang(mabaidang)

def getAllCamXucBaiDangNhomByMaNguoiDung(manguoidung):
    return CamXucBaiDangNhomRepository.GetAllByMaNguoiDung(manguoidung)

def findCamXucBaiDangNhomById(id):
    return CamXucBaiDangNhomRepository.FindById(id)

def deleteCamXucBaiDangNhom(id):
    return CamXucBaiDangNhomRepository.Delete(id)