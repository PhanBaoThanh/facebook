from app.models import Comment
from app import db
from datetime import datetime
from sqlalchemy import desc
def Create(mabaidang, manguoidung , noidung):
    comment = Comment(PostId = mabaidang, ClientId = manguoidung, Content = noidung, CreatedAt = datetime.now())
    db.session.add(comment)
    db.session.commit()
    return comment

def Update(maComment, noidung):
    comment = Comment.query.filter(Comment.CommentId == maComment).first()
    comment.Content = noidung
    db.session.commit()
    return comment

def GetAllByPostId(mabaidang):
    return Comment.query.filter(Comment.PostId == mabaidang).order_by(desc(Comment.CreatedAt)).all()

def FindById(id):
    return Comment.query.filter(Comment.CommentId == id).first_or_404()

def Delete(id):
    comment = Comment.query.filter(Comment.CommentId == id).first()
    db.session.delete(comment)
    db.session.commit()
    return "Deleted"

def DeleteByPostId(postId):
    comments = Comment.query.filter(Comment.PostId == postId).all()
    for comment in comments:
        db.session.delete(comment)
    db.session.commit()
    return "Deleted"