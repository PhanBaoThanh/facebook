from app import db, login
from flask_login import UserMixin
import datetime
import json
from json import JSONEncoder

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

@login.user_loader
def load_user(id):
    return NguoiDung.query.get(int(id))

class Admin(UserMixin, db.Model):
    __tablename__ = 'Admin'
    MaAdmin = db.Column(db.Integer, primary_key = True)
    HoTen = db.Column(db.String(128))
    NgaySinh = db.Column(db.DateTime)
    TaiKhoan = db.Column(db.String(128))
    MatKhau = db.Column(db.String(128))     
    
    def get_id(self):
        return self.MaAdmin
    
    def serialize(self):
        return {
            'maAdmin': self.MaAdmin,
            'hoTen': self.HoTen,
            'ngaySinh': json.dumps(self.NgaySinh, indent=4, cls= DateTimeEncoder),
            'taiKhoan': self.TaiKhoan,
            'matKhau': self.MatKhau
        }
        
class NguoiDung(UserMixin, db.Model):
    __tablename__ ='NguoiDung'
    MaNguoiDung = db.Column(db.Integer, primary_key = True)
    HoTen = db.Column(db.String(128))
    SDT = db.Column(db.String(128))
    Email = db.Column(db.String(128))
    TaiKhoan = db.Column(db.String(128))
    MatKhau = db.Column(db.String(128))
    GioiTinh = db.Column(db.Boolean)
    NgaySinh = db.Column(db.DateTime)
    Anh = db.Column(db.String(500))
    AnhBia = db.Column(db.String(500))

    def get_id(self):
        return self.MaNguoiDung
    
    def serialize(self):
        return {
            'maNguoiDung': self.MaNguoiDung,
            'hoTen': self.HoTen,
            'sdt': self.SDT,
            'email': self.Email,
            'taiKhoan': self.TaiKhoan,
            'matKhau': self.MatKhau,
            'gioiTinh': self.GioiTinh,
            'ngaySinh': json.dumps(self.NgaySinh,indent=4,cls=DateTimeEncoder),
            'anh': self.Anh,
            'anhBia': self.AnhBia
        }
    
class Nhom(db.Model):
    __tablename__ = "Nhom"
    MaNhom = db.Column(db.Integer,primary_key = True)
    MaQuanTriVien = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    TenNhom = db.Column(db.String(128))
    NgayTao = db.Column(db.DateTime)
    Anh = db.Column(db.String(500))
    AnhBia = db.Column(db.String(500))
    RiengTu = db.Column(db.Boolean)
    
    def get_id(self):
        return self.MaNhom
    
    def serialize(self):
        return {
            "maNhom": self.MaNhom,
            "maQuanTriVien": self.MaQuanTriVien,
            "tenNhom": self.TenNhom,
            "ngayTao": json.dumps(self.NgayTao, indent=4 , cls=DateTimeEncoder),
            "anh": self.Anh,
            "anhBia": self.AnhBia,
            "riengTu": self.RiengTu
        }
        
class TinNhan(db.Model):
    __tablename__ = "TinNhan"
    MaTinNhan = db.Column(db.Integer, primary_key = True)
    NguoiGui = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    NguoiNhan = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    NoiDung = db.Column(db.String(500))
    ThoiGianGui = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MaTinNhan
    
    def serialize(self):
        return {
            "maTinNhan": self.MaTinNhan,
            "nguoiGui": self.NguoiGui,
            "nguoiNhan": self.NguoiNhan,
            "noiDung": self.NoiDung,
            "thoiGianGui": json.dumps(self.ThoiGianGui, indent=4, cls=DateTimeEncoder)
        }
        
class Friend(db.Model):
    __tablename__ = 'Friend'
    MaBan = db.Column(db.Integer, primary_key = True)
    MaNguoiDung1 = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    MaNguoiDung2 = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    
    def get_id(self):
        return self.MaBan
    
    def serialize(self):
        return {
            'maBan': self.MaBan,
            'maNguoiDung1': self.MaNguoiDung1,
            'maNguoiDung2': self.MaNguoiDung2
        }
    
class ThanhVienNhom(db.Model):
    __tablename__ = 'ThanhVienNhom'
    MaThanhVienNhom = db.Column(db.Integer, primary_key = True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    
    def get_id(self):
        return self.MaThanhVienNhom
    
    def serialize(self):
        return {
            'maThanhVienNhom': self.MaThanhVienNhom,
            'maNhom': self.MaNhom,
            'maNguoiDung': self.MaNguoiDung
        }

class BaiDangCaNhan(db.Model):
    __tablename__ = 'BaiDangCaNhan'
    MaBaiDang = db.Column(db.Integer, primary_key = True)
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    ThoiGianDang = db.Column(db.DateTime)
    NoiDung = db.Column(db.String(500))
    Anh = db.Column(db.String(500))
    
    def get_id(self):
        return self.MaBaiDang
    
    def serialize(self):
        return {
            'maBaiDang': self.MaBaiDang,
            'maNguoiDung': self.MaNguoiDung,
            'thoiGianDang': json.dumps(self.ThoiGianDang, indent=4, cls=DateTimeEncoder),
            'noiDung': self.NoiDung,
            'anh': self.Anh
        }
    
class BaiDangNhom(db.Model):
    __tablename__ = 'BaiDangNhom'
    MaBaiDang = db.Column(db.Integer, primary_key = True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    ThoiGianDang = db.Column(db.DateTime)
    NoiDung = db.Column(db.String(500))
    Anh = db.Column(db.String(500))
    
    def get_id(self):
        return self.MaBaiDang
    
    def serialize(self):
        return {
            'maBaiDang': self.MaBaiDang,
            'maNhom': self.MaNhom,
            'maNguoiDung': self.MaNguoiDung,
            'thoiGianDang': json.dumps(self.ThoiGianDang, indent=4 , cls = DateTimeEncoder),
            'noiDung': self.NoiDung,
            'anh': self.Anh
        }
    
class CamXucBaiDangCaNhan(db.Model):
    __tablename__ = 'CamXucBaiDangCaNhan'
    MaCamXuc = db.Column(db.Integer, primary_key = True)
    MaBaiDang = db.Column(db.Integer, db.ForeignKey('BaiDangCaNhan.MaBaiDang'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    
    def get_id(self):
        return self.MaCamXuc
    
    def serialize(self):
        return {
            'maCamXuc': self.MaCamXuc,
            'maBaiDang': self.MaBaiDang,
            'maNguoiDung': self.MaNguoiDung
        }
    
class CamXucBaiDangNhom(db.Model):
    __tablename__ = 'CamXucBaiDangNhom' 
    MaCamXuc = db.Column(db.Integer, primary_key = True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaBaiDang = db.Column(db.Integer, db.ForeignKey('BaiDangCaNhan.MaBaiDang'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    
    def get_id(self):
        return self.MaCamXuc

    def serialize(self):
        return {
            'maCamXuc': self.MaCamXuc,
            'maNhom': self.MaNom,
            'maBaiDang': self.MaBaiDang,
            'maNguoiDung': self.MaNguoiDung
        }

class BinhLuanBaiDangCaNhan(db.Model):
    __tablename__ = 'BinhLuanBaiDangCaNhan'
    MaBinhLuan = db.Column(db.Integer, primary_key = True)
    MaBaiDang = db.Column(db.Integer, db.ForeignKey('BaiDangCaNhan.MaBaiDang'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    NoiDung = db.Column(db.String(500))
    ThoiGian = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MaBinhLuan
    
    def serialize(self):
        return {
            'maBinhLuan': self.MaBinhLuan,
            'maBaiDang': self.MaBaiDang,
            'maNguoiDung': self.MaNguoiDung,
            'noiDung': self.NoiDung,
            'thoiGian': json.dumps(self.ThoiGian, indent=4, cls=DateTimeEncoder)
        }
    
    
    
class BinhLuanBaiDangNhom(db.Model):
    __tablename__ = 'BinhLuanBaiDangNhom'
    MaBinhLuan = db.Column(db.Integer, primary_key = True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaBaiDang = db.Column(db.Integer, )
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    NoiDung = db.Column(db.String(500))
    ThoiGian = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MaBinhLuan
    
    def serialize(self):
        return {
            'maBinhLuan': self.MaBinhLuan,
            'maNhom': self.MaNhom,
            'maBaiDang': self.MaBaiDang,
            'maNguoiDung': self.MaNguoiDung,
            'noiDung': self.NoiDung,
            'thoiGian': json.dumps(self.ThoiGian, indent=4, cls=DateTimeEncoder)
        }
    
class YeuCauKetBan(db.Model):
    __tablename__ = 'YeuCauKetBan'
    MaYeuCauKetBan = db.Column(db.Integer, primary_key = True)
    MaNguoiGui = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    MaNguoiNhan = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    ThoiGianGui = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MaYeuCauKetBan
    
    def serialize(self):
        return {
            'maYeuCauKetBan': self.MaYeuCauKetBan,
            'maNguoiGui': self.MaNguoiGui,
            'maNguoiNhan': self.MaNguoiNhan,
            'thoiGianGui': json.dumps(self.ThoiGianGui, indent=4, cls = DateTimeEncoder)
        }
class YeuCauThamGiaNhom(db.Model):
    __tablename__ = 'YeuCauThamGiaNhom'
    MaYeuCauThamGiaNhom = db.Column(db.Integer, primary_key = True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    ThoiGianGui = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MaYeuCauThamGiaNhom

    def serialize(self):
        return {
            'maYeuCauThamGiaNhom': self.MaYeuCauThamGiaNhom,
            'maNhom': self.MaNhom,
            'maNguoiDung': self.MaNguoiDung,
            'thoiGianGui': json.dumps(self.ThoiGianGui, indent=4, cls=DateTimeEncoder)
        }
    
class XetDuyetBaiDangNhom(db.Model):
    __tablename__ = 'XetDuyetBaiDangNhom'
    MaXetDuyet = db.Column(db.Integer, primary_key=True)
    MaNhom = db.Column(db.Integer, db.ForeignKey('Nhom.MaNhom'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('NguoiDung.MaNguoiDung'))
    ThoiGianDang = db.Column(db.DateTime)
    NoiDung = db.Column(db.String(500))
    Anh = db.Column(db.String(500))
    
    def get_id(self):
        return self.MaXetDuyet
    
    def serialize(self):
        return {
            'maXetDuyet': self.MaXetDuyet,
            'maNhom': self.MaNhom,
            'maNguoiDung': self.MaNguoiDung,
            'thoiGianDang': json.dumps(self.ThoiGianDang, indent=4, cls=DateTimeEncoder),
            'noiDung': self.NoiDung,
            'anh': self.Anh
        }