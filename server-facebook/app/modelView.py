from app import db
import datetime
import json
from json import JSONEncoder

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

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
