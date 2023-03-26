from app.Repository import BinhLuanBaiDangCaNhanRepository

def createBinhLuanBaiDangCaNhan(mabaidang,manguoidung,noidung):
    return BinhLuanBaiDangCaNhanRepository.Create(mabaidang,manguoidung,noidung)

def updateBinhLuanBaiDangCaNhan(mabinhluanbaidangcanhan,noidung):
    return BinhLuanBaiDangCaNhanRepository.Update(mabinhluanbaidangcanhan,noidung)

def getAllBinhLuanBaiDangCaNhanByMaBaiDang(mabaidang):
    return BinhLuanBaiDangCaNhanRepository.GetAllByMaBaiDang(mabaidang)

def findBinhLuanBaiDangCaNhanById(id):
    return BinhLuanBaiDangCaNhanRepository.FindById(id)

def deleteBinhLuanBaiDangCaNhan(id):
    return BinhLuanBaiDangCaNhanRepository.Delete(id)