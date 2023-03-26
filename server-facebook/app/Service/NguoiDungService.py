from app.Repository import NguoiDungRepository

def createNguoiDung(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia):
    return NguoiDungRepository.Create(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia)

def updateNguoiDung(hoten,sdt,email,taikhoan,gioitinh,ngaysinh):
    return NguoiDungRepository.Update(hoten,sdt,email,taikhoan,gioitinh,ngaysinh)

def deleteNguoiDung(id):
    return NguoiDungRepository.Delete(id)

def updatePassword(taikhoan,matkhau):
    return NguoiDungRepository.UpdatePassword(taikhoan,matkhau)

def updateAvatar(taikhoan,avt):
    return NguoiDungRepository.UpdateAvatar(taikhoan,avt)

def updateBackgroundImage(taikhoan,backgroundImg):
    return NguoiDungRepository.UpdateBackgroundImage(taikhoan,backgroundImg)

def findNguoiDungById(id):
    return NguoiDungRepository.findById(id)

def searchNguoiDung(key):
    return NguoiDungRepository.Search(key)

def checkLoginNguoiDung(taikhoan,matkhau):
    return NguoiDungRepository.checkLogin(taikhoan,matkhau)