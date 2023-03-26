import sqlite3
from sqlite3 import Error
from app.modelView import GroupInfo,ClientInfo,MemberInfo

def GetAllGroupByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute("select Groups.GroupId,Name,CreatedAt,BackgroundImg,IsPrivate from Groups inner join GroupMember on Groups.GroupId = GroupMember.GroupId where GroupMember.ClientId = ?",[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(GroupInfo(GroupId = row[0],Name=row[1],CreatedAt=row[2],BackgroundImg=row[3],IsPrivate=row[4]).serialize())
    cursor.close()
    return list

def GetAllGroupByGroupRequest(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('select Groups.GroupId,Name,GroupRequest.CreatedAt,BackgroundImg,IsPrivate from Groups join GroupRequest on Groups.GroupId = GroupRequest.GroupId where ClientId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(GroupInfo(GroupId = row[0],Name=row[1],CreatedAt=row[2],BackgroundImg=row[3],IsPrivate=row[4]).serialize())
    cursor.close()
    return list

def GetFriendByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg from Client inner join Friend on Client.ClientId = Friend.ClientId1 where Friend.ClientId2 = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(ClientInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9]).serialize())
    cursor.close()
    return list

def GetFriendByFriendRequest(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg from Client join FriendRequest on Client.ClientId = FriendRequest.ReceiverId where FriendRequest.SenderId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(ClientInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9]).serialize())
    cursor.close()
    return list

def GetFriendByFriendResponse(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg from Client join FriendRequest on Client.ClientId = FriendRequest.SenderId where FriendRequest.ReceiverId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(ClientInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9]).serialize())
    cursor.close()
    return list

def GetAllClientFromGroupMember(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupId,IsAdmin from Client join GroupMember on Client.ClientId = GroupMember.ClientId where GroupId = ?',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(MemberInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],GroupId=row[10],IsAdmin=row[11]).serialize())
    cursor.close()
    return list

def GetAllMemberFromGroupRequest(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupId from Client join GroupRequest on Client.ClientId = GroupRequest.ClientId where GroupId = ?',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(MemberInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],GroupId=row[10],IsAdmin=False).serialize())
    cursor.close()
    return list