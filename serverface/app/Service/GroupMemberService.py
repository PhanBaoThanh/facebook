from app.Repository import GroupMemberRepository

def createGroupMember(manhom,manguoidung,isAdmin):
    return GroupMemberRepository.Create(manhom,manguoidung,isAdmin)

def updateGroupMember(manhom,manguoidung,isAdmin):
    return GroupMemberRepository.Update(manhom,manguoidung,isAdmin)

def getAllGroupMemberByGroupId(manhom):
    return GroupMemberRepository.GetAllByGroupId(manhom)

def getAllGroupMemberByClientId(manguoidung):
    return GroupMemberRepository.GetAllByClientId(manguoidung)

def findGroupMemberByClientIdAndGroupId(clientId,groupId):
    return GroupMemberRepository.FindGroupMemberByClientIdAndGroupId(clientId,groupId)

def findGroupMemberById(id):
    return GroupMemberRepository.FindById(id)

def deleteGroupMember(id):
    return GroupMemberRepository.Delete(id)

def deleteGroupMemberByClientIdAndGroupId(clientId,groupId):
    return GroupMemberRepository.DeleteByClientIdAndGroupId(clientId,groupId)

def deleteGroupMemberAndUpdateNewAdmin(clientId,groupId,adminId):
    return GroupMemberRepository.DeleteAndUpdateNewAdmin(clientId,groupId,adminId)