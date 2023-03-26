from app import db
import datetime
import json
from json import JSONEncoder

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

class GroupInfo():
    GroupId = ""
    Name = ""
    CreatedAt = ""
    BackgroundImg = ""
    IsPrivate = ""
    
    def __init__(self,GroupId,Name,CreatedAt,BackgroundImg,IsPrivate):
        self.GroupId = GroupId
        self.Name = Name
        self.CreatedAt = CreatedAt
        self.BackgroundImg = BackgroundImg
        self.IsPrivate = IsPrivate
        
    def serialize(self):
        return {
            'groupId': self.GroupId,
            'name': self.Name,
            'createdAt': self.CreatedAt,
            'backgroundImg': self.BackgroundImg,
            'isPrivate': self.IsPrivate
        }
        
class ClientInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg
        }
        
class MemberInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    GroupId = ""
    IsAdmin = False
    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupId,IsAdmin):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        self.GroupId = GroupId
        self.IsAdmin = IsAdmin
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg,
            'groupId': self.GroupId,
            'isAdmin': self.IsAdmin
        }

class TinNhanView():
    MaTinNhan = ""
    
    def __init__(self,MaTinNhan):
        self.MaTinNhan = MaTinNhan

class BaiDangView():
    MaBaiDang = ""
    MaNhom = ""
    MaNguoiDung = ""
    ThoiGianDang = ""
    NoiDung = ""
    Anh = ""
    IsNhom = False
    
    def __init__(self,MaBaiDang,MaNhom,MaNguoiDung,ThoiGianDang,NoiDung,Anh,IsNhom):
        self.MaBaiDang = MaBaiDang
        self.MaNhom = MaNhom
        self.MaNguoiDung = MaNguoiDung
        self.ThoiGianDang = ThoiGianDang
        self.NoiDung = NoiDung
        self.Anh = Anh
        self.IsNhom = IsNhom
        
    def serialize(self):
        return {
            'maBaiDang': self.MaBaiDang,
            'maNhom': self.MaNhom,
            'maNguoiDung': self.MaNguoiDung,
            'thoiGianDang': json.dumps(self.ThoiGianDang, indent=4, cls= DateTimeEncoder),
            'noiDung': self.NoiDung,
            'anh': self.Anh,
            'isNhom': self.IsNhom
        }
        
class NhomView():
    MaNhom = ""
    
    def __init__(self,MaNhom):
        self.MaNhom = MaNhom
        
class BanBeView():
    MaBanBe = ""
    
    def __init__(self,MaBanBe):
        self.MaBanBe = MaBanBe
