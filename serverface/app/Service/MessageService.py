from app.Repository import MessageRepository

def createMessage(nguoigui,nguoinhan,noidung):
    return MessageRepository.Create(nguoigui,nguoinhan,noidung)

def getAllMessageByClientId(nguoidung1,nguoidung2):
    return MessageRepository.GetAllByClientId(nguoidung1,nguoidung2)

def findMessageById(id):
    return MessageRepository.FindById(id)

def deleteMessage(id):
    return MessageRepository.Delete(id)