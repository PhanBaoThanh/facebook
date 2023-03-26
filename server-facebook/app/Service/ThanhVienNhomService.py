from app.Repository import ThanhVienNhomRepository

def createThanhVienNhom(manhom,manguoidung):
    return ThanhVienNhomRepository.Create(manhom,manguoidung)

def getAllThanhVienNhomByMaNhom(manhom):
    return ThanhVienNhomRepository.GetAllByMaNhom(manhom)

def findThanhVienNhomById(id):
    return ThanhVienNhomRepository.FindById(id)

def findAllThanhVienNhomByMaNguoiDung(manguoidung):
    return ThanhVienNhomRepository.FindAllByMaNguoiDung(manguoidung)

def deleteThanhVienNhom(id):
    return ThanhVienNhomRepository.Delete(id)