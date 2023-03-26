from app.Repository import GroupRequestRepository

def createGroupRequest(manhom,manguoidung):
    return GroupRequestRepository.Create(manhom,manguoidung)

def getAllGroupRequestByClientId(manguoidung):
    return GroupRequestRepository.GetAllByClientId(manguoidung)

def getAllGroupRequestByGroupId(manhom):
    return GroupRequestRepository.GetAllByGroupId(manhom)

def findGroupRequestById(id):
    return GroupRequestRepository.FindById(id)

def findGroupRequestByClientIdAndGroupId(clientId,groupId):
    return GroupRequestRepository.FindByClientIdAndGroupId(clientId,groupId)

def confirmGroupRequest(id):
    return GroupRequestRepository.Confirm(id)

def confirmGroupRequestByClientIdAdnGroupId(clientId,groupId):
    return GroupRequestRepository.ConfirmByClientIdAndGroupId(clientId,groupId)

def deleteGroupRequest(id):
    return GroupRequestRepository.Delete(id)

def deleteByClientIdAndGroupId(clientId,groupId):
    return GroupRequestRepository.DeleteByClientIdAndGroupId(clientId,groupId)


    