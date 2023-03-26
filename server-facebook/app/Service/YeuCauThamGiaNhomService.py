from app.Repository import YeuCauThamGiaNhomRepository

def createYeuCauThamGiaNhom(manhom,manguoidung):
    return YeuCauThamGiaNhomRepository.Create(manhom,manguoidung)

def getAllYeuCauThamGiaNhomByMaNguoiDung(manguoidung):
    return YeuCauThamGiaNhomRepository.GetAllByMaNguoiDung(manguoidung)

def getAllYeuCauThamGiaNhomByMaNhom(manhom):
    return YeuCauThamGiaNhomRepository.GetAllByMaNhom(manhom)

def findYeuCauThamGiaNhomById(id):
    return YeuCauThamGiaNhomRepository.FindById(id)

def deleteYeuCauThamGiaNhom(id):
    return YeuCauThamGiaNhomRepository.Delete(id)


    