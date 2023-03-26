from app.Repository import XetDuyetBaiDangNhomRepository

def createXetDuyetBaiDangNhom(manhom,manguoidung,noidung,anh):
    return XetDuyetBaiDangNhomRepository.Create(manhom,manguoidung,noidung,anh)

def getAllXetDuyetBaiDangNhomByMaNhom(manhom):
    return XetDuyetBaiDangNhomRepository.GetAllByMaNhom(manhom)

def findXetDuyetBaiDangNhomById(id):
    return XetDuyetBaiDangNhomRepository.FindById(id)

def deleteXetDuyetBaiDangNhom(id):
    return XetDuyetBaiDangNhomRepository.Delete(id)

def confirmed(id):
    return XetDuyetBaiDangNhomRepository.Confirm(id)