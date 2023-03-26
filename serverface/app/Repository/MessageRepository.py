from app.models import Message
from app import db
from datetime import datetime
from sqlalchemy import or_,and_

def Create(nguoigui,nguoinhan,noidung):
    message = Message(SenderId = nguoigui, ReceiverId = nguoinhan, Content = noidung, CreatedAt = datetime.now())
    db.session.add(message)
    db.session.commit()
    return message

def GetAllByClientId(nguoidung1, nguoidung2):
    return Message.query.filter(or_(and_(Message.SenderId == nguoidung1, Message.ReceiverId == nguoidung2),and_(Message.SenderId == nguoidung2 ,Message.ReceiverId == nguoidung1))).order_by(Message.CreatedAt.asc()).all()

def FindById(id):
    return Message.query.filter(Message.MessageId == id).first_or_404()

def Delete(id):
    message = Message.get_id(id)
    db.session.delete(message)
    db.session.commit()
    return "Deleted"