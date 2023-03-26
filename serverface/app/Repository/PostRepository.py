from app.models import Post,Friend
from app.Repository import ReactionRepository,CommentRepository
from app import db
from datetime import datetime
from sqlalchemy import or_,desc

def Create(manhom,manguoidung,  noidung, anh):
    post = Post(GroupId = manhom, ClientId = manguoidung, CreatedAt = datetime.now(), Content = noidung, Img = anh)
    db.session.add(post)
    db.session.commit()
    return post

def Update(maPost, noidung, anh):
    post = Post.query.filter(Post.PostId == maPost).first()
    post.Content = noidung
    post.Img = anh
    db.session.commit()
    return post

def GetAllPostOfFriend(clientId):
    friends = Friend.query.filter(Friend.ClientId1 == clientId).all()
    friendIds = []
    for friend in friends:
        friendIds.append(friend.ClientId2)
    return Post.query.filter(Post.ClientId.in_(friendIds)).order_by(Post.CreatedAt.desc()).all()

def GetAllOfClient(manguoidung):
    return Post.query.filter(Post.ClientId == manguoidung,Post.GroupId == None).order_by(desc(Post.CreatedAt)).all()

def GetAllOfGroup(manhom):
    return Post.query.filter(Post.GroupId == manhom).order_by(Post.CreatedAt.desc()).all()

def GetAllByClientIdAndGroupId(manhom,manguoidung):
    return Post.query.filter(Post.GroupId == manhom, Post.ClientId == manguoidung).order_by(Post.CreatedAt.desc()).all()

def FindById(id):
    return Post.query.filter(Post.PostId == id).first_or_404()

def Search(key):
    return Post.query.filter(Post.Content.like('%' + key + '%')).order_by(Post.CreatedAt.desc()).all()

def Delete(id):
    # ReactionRepository.DeleteByPostId(postId = id)
    # CommentRepository.DeleteByPostId(postId = id)
    post = Post.query.filter(Post.PostId == id).first()
    db.session.delete(post)
    db.session.commit()
    return "Deleted"

def DeleteByGroupId(groupId):
    PostOfGroup = GetAllOfGroup(groupId)
    