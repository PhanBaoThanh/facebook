from app.Repository import YeuCauKetBanRepository

def createYeuCauKetBan(nguoinhan,nguoigui):
    return YeuCauKetBanRepository.Create(nguoinhan,nguoigui)

def getAllYeuCauKetBanByMaNguoiNhan(manguoinhan):
    return YeuCauKetBanRepository.GetAllByMaNguoiNhan(manguoinhan)

def getAllYeuCauKetBanByMaNguoiGui(manguoigui):
    return YeuCauKetBanRepository.GetAllByMaNguoiGui(manguoigui)

def findYeuCauKetBanById(id):
    return YeuCauKetBanRepository.FindById(id)

def deleteYeuCauKetBan(id):
    return YeuCauKetBanRepository.Delete(id)