from app.Repository import BaiDangNhomRepository

def createBaiDangNhom(manhom,manguoidung,noidung,anh):
    return BaiDangNhomRepository.Create(manhom,manguoidung,noidung,anh)

def updateBaiDangNhom(mabaidangnhom, noidung, anh):
    return BaiDangNhomRepository.Update(mabaidangnhom,noidung,anh)

def getAllBaiDangNhomByMaNhom(manhom):
    return BaiDangNhomRepository.GetAllByMaNhom(manhom)

def findBaiDangNhomById(id):
    return BaiDangNhomRepository.FindById(id)

def findBaiDangNhomByKey(key):
    return BaiDangNhomRepository.FindByKey(key)

def findBaiDangNhomByMaNguoiDung(manhom,manguoidung):
    return BaiDangNhomRepository.FindByMaNguoiDung(manhom,manguoidung)

def deleteBaiDangNhom(id):
    return BaiDangNhomRepository.Delete(id)