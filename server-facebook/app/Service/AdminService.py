from app.Repository import AdminRepository

def createAdmin(username,password,name,dayOfBirth):
    return AdminRepository.Create(username,password,name,dayOfBirth)

def updateAdmin(username,password,name,dayOfBirth):
    return AdminRepository.Update(username,password,name,dayOfBirth)

def deleteAdmin(id):
    return AdminRepository.Delete(id)

def checkLoginAdmin(username,password):
    return AdminRepository.checkLogin(username,password)