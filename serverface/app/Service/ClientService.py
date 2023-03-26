from app.Repository import ClientRepository

def createClient(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia):
    return ClientRepository.Create(hoten,sdt,email,taikhoan,matkhau,gioitinh,ngaysinh,anh,anhbia)

def updateClient(clientId,hoten,sdt,email,gioitinh,ngaysinh):
    return ClientRepository.Update(clientId,hoten,sdt,email,gioitinh,ngaysinh)

def deleteClient(id):
    return ClientRepository.Delete(id)

def updatePassword(clientId,matkhaucu,matkhaumoi):
    return ClientRepository.UpdatePassword(clientId,matkhaucu,matkhaumoi)

def updateAvatar(clientId,avt):
    return ClientRepository.UpdateAvatar(clientId,avt)

def updateBackgroundImage(clientId,backgroundImg):
    return ClientRepository.UpdateBackgroundImage(clientId,backgroundImg)

def findClientById(id):
    return ClientRepository.findById(clientId= id)

def searchClient(key,clientId):
    return ClientRepository.Search(key,clientId)

def checkLoginClient(taikhoan,matkhau):
    return ClientRepository.checkLogin(taikhoan,matkhau)