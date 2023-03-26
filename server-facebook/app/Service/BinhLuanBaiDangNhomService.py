from app.Repository import BinhLuanBaiDangNhomRepository

def createBinhLuanBaiDangNhom(manhom,mabaidang,manguoidung,noidung):
    return BinhLuanBaiDangNhomRepository.Create(manhom,mabaidang,manguoidung,noidung)

def updateBinhLuanBaiDangNhom(mabinhluanbaidangnhom, noidung):
    return BinhLuanBaiDangNhomRepository.Update(mabinhluanbaidangnhom,noidung)

def getAllBinhLuanBaiDangNhomByMaBaiDang(mabaidang,manhom):
    return BinhLuanBaiDangNhomRepository.GetAllByMaBaiDang(mabaidang,manhom)

def findBinhLuanBaiDangNhomById(id):
    return BinhLuanBaiDangNhomRepository.FindById(id)

def deleteBinhLuanBaiDangNhom(id):
    return BinhLuanBaiDangNhomRepository.Delete(id)