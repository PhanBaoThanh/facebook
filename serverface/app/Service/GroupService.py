from app.Repository import GroupRepository

def createGroup(tennhom,anhbia,riengtu):
    return GroupRepository.Create(tennhom,anhbia,riengtu)

def updateGroup(manhom,tennhom,riengtu):
    return GroupRepository.Update(manhom,tennhom,riengtu)

def deleteGroup(id):
    return GroupRepository.Delete(id)


def updateBackgroundImage(manhom,backgroundImg):
    return GroupRepository.UpdateBackgroundImage(manhom,backgroundImg)

def findGroupById(id):
    return GroupRepository.findById(id)

def searchGroup(key):
    return GroupRepository.Search(key)