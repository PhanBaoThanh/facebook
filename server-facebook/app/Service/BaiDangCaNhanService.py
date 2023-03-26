from app.Repository import BaiDangCaNhanRepository

def createBaiDangCaNhan(manguoidung,noidung,anh):
    return BaiDangCaNhanRepository.Create(manguoidung,noidung,anh)

def updateBaiDangCaNhan(mabaidangcanhan, noidung, anh):
    return BaiDangCaNhanRepository.Update(mabaidangcanhan,noidung,anh)

def getAllBaiDangCaNhanByMaNguoiDung(manguoidung):
    return BaiDangCaNhanRepository.GetAllByMaNguoiDung(manguoidung)

def findBaiDangCaNhanById(id):
    return BaiDangCaNhanRepository.FindById(id)

def findBaiDangCaNhanByKey(key):
    return BaiDangCaNhanRepository.FindByKey(key)

def deleteBaiDangCaNhan(id):
    return BaiDangCaNhanRepository.Delete(id)