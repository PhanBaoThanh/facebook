from app import app
from app import db
from flask import Flask
from app.models import NguoiDung,Admin,BaiDangCaNhan,BaiDangNhom,BinhLuanBaiDangCaNhan,BinhLuanBaiDangNhom,CamXucBaiDangCaNhan,CamXucBaiDangNhom,Friend,Nhom,ThanhVienNhom,TinNhan,YeuCauKetBan,YeuCauThamGiaNhom,XetDuyetBaiDangNhom

@app.shell_context_processor
def pro_shell_context():
    return {
        'db': db,
        'NguoiDung': NguoiDung,
        'Admin': Admin,
        'Nhom': Nhom,
        'Friend': Friend,
        'ThanhVienNhom': ThanhVienNhom,
        'TinNhan': TinNhan,
        'BaiDangCaNhan': BaiDangCaNhan,
        'BaiDangNhom': BaiDangNhom,
        'BinhLuanBaiDangCaNhan': BinhLuanBaiDangCaNhan,
        'BinhLuanBaiDangNhom': BinhLuanBaiDangNhom,
        'CamXucBaiDangCaNhan': CamXucBaiDangCaNhan,
        'CamXucBaiDangNhom': CamXucBaiDangNhom,
        'YeuCauKetBan': YeuCauKetBan,
        'YeuCauThamGiaNhom': YeuCauThamGiaNhom,
        'XetDuyetBaiDangNhom': XetDuyetBaiDangNhom
    }
