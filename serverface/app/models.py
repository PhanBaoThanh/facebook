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
    return Client.query.get(int(id))

class Admin(UserMixin, db.Model):
    __tablename__ = 'Admin'
    AdminId = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128))
    DateOfBirth = db.Column(db.DateTime)
    Account = db.Column(db.String(128))
    Password = db.Column(db.String(128))     
    
    def get_id(self):
        return self.AdminId
    
    def serialize(self):
        return {
            'adminId': self.AdminId,
            'Name': self.Name,
            'dayOfBirth': json.dumps(self.DateOfBirth, indent=4, cls= DateTimeEncoder),
            'account': self.Account,
            'password': self.Password
        }
        
class Client(UserMixin, db.Model):
    __tablename__ ='Client'
    ClientId = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128))
    PhoneNumber = db.Column(db.String(128))
    Email = db.Column(db.String(128))
    Account = db.Column(db.String(128))
    Password = db.Column(db.String(128))
    Sex = db.Column(db.Boolean)
    DayOfBirth = db.Column(db.DateTime)
    Avatar = db.Column(db.String(500))
    BackgroundImg = db.Column(db.String(500))

    def get_id(self):
        return self.ClientId
    
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': json.dumps(self.DayOfBirth,indent=4,cls=DateTimeEncoder),
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg
        }
    
class Group(db.Model):
    __tablename__ = "Groups"
    GroupId = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String(128))
    CreatedAt = db.Column(db.DateTime)
    BackgroundImg = db.Column(db.String(500))
    IsPrivate = db.Column(db.Boolean)
    posts = db.relationship("Post", cascade='all, delete')
    groupMembers = db.relationship("GroupMember", cascade='all, delete')
    groupRequests = db.relationship("GroupRequest", cascade='all, delete')
    postConfirms = db.relationship("PostConfirm", cascade='all, delete')
    
    def get_id(self):
        return self.GroupId
    
    def serialize(self):
        return {
            "groupId": self.GroupId,
            "name": self.Name,
            "createdAt": json.dumps(self.CreatedAt, indent=4 , cls=DateTimeEncoder),
            "backgroundImg": self.BackgroundImg,
            "isPrivate": self.IsPrivate
        }
        
class Message(db.Model):
    __tablename__ = "Message"
    MessageId = db.Column(db.Integer, primary_key = True)
    SenderId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    ReceiverId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    Content = db.Column(db.String(500))
    CreatedAt = db.Column(db.DateTime)
    
    def get_id(self):
        return self.MessageId
    
    def serialize(self):
        return {
            "messageId": self.MessageId,
            "senderId": self.SenderId,
            "receivedId": self.ReceiverId,
            "content": self.Content,
            "createdAt": json.dumps(self.CreatedAt, indent=4, cls=DateTimeEncoder)
        }
        
class Friend(db.Model):
    __tablename__ = 'Friend'
    FriendId = db.Column(db.Integer, primary_key = True)
    ClientId1 = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    ClientId2 = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    
    def get_id(self):
        return self.FriendId
    
    def serialize(self):
        return {
            'friendId': self.FriendId,
            'clientId1': self.ClientId1,
            'clientId2': self.ClientId2
        }
    
class GroupMember(db.Model):
    __tablename__ = 'GroupMember'
    GroupMemberId = db.Column(db.Integer, primary_key = True)
    GroupId = db.Column(db.Integer, db.ForeignKey('Groups.GroupId',ondelete='CASCADE'))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    IsAdmin = db.Column(db.Boolean)
    
    def get_id(self):
        return self.GroupMemberId
    
    def serialize(self):
        return {
            'groupMemberId': self.GroupMemberId,
            'groupId': self.GroupId,
            'clientId': self.ClientId,
            'isAdmin': self.IsAdmin
        }
    
class Post(db.Model):
    __tablename__ = 'Post'
    PostId = db.Column(db.Integer, primary_key = True)
    GroupId = db.Column(db.Integer, db.ForeignKey('Groups.GroupId', ondelete="CASCADE"))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    CreatedAt = db.Column(db.DateTime)
    Content = db.Column(db.String(500))
    Img = db.Column(db.String(500))
    reactions = db.relationship("Reaction", cascade="all, delete")
    comments = db.relationship("Comment", cascade="all, delete")
    
    def get_id(self):
        return self.PostId
    
    def serialize(self):
        return {
            'postId': self.PostId,
            'groupId': self.GroupId,
            'clientId': self.ClientId,
            'createdAt': json.dumps(self.CreatedAt, indent=4 , cls = DateTimeEncoder),
            'content': self.Content,
            'img': self.Img
        }
    
class Reaction(db.Model):
    __tablename__ = 'Reaction'
    ReactionId = db.Column(db.Integer, primary_key = True)
    PostId = db.Column(db.Integer, db.ForeignKey('Post.PostId',ondelete='CASCADE'))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    
    def get_id(self):
        return self.ReactionId
    
    def serialize(self):
        return {
            'reactionId': self.ReactionId,
            'postId': self.PostId,
            'clientId': self.ClientId
        }

class Comment(db.Model):
    __tablename__ = 'Comment'
    CommentId = db.Column(db.Integer, primary_key = True)
    PostId = db.Column(db.Integer, db.ForeignKey('Post.PostId',ondelete='CASCADE'))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    Content = db.Column(db.String(500))
    CreatedAt = db.Column(db.DateTime)
    
    def get_id(self):
        return self.CommentId
    
    def serialize(self):
        return {
            'commentId': self.CommentId,
            'postId': self.PostId,
            'clientId': self.ClientId,
            'content': self.Content,
            'createdAt': json.dumps(self.CreatedAt, indent=4, cls=DateTimeEncoder)
        }
    
class FriendRequest(db.Model):
    __tablename__ = 'FriendRequest'
    FriendRequestId = db.Column(db.Integer, primary_key = True)
    SenderId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    ReceiverId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    CreatedAt = db.Column(db.DateTime)
    
    def get_id(self):
        return self.FriendRequestId
    
    def serialize(self):
        return {
            'friendRequestId': self.FriendRequestId,
            'senderId': self.SenderId,
            'receiverId': self.ReceiverId,
            'createdId': json.dumps(self.CreatedAt, indent=4, cls = DateTimeEncoder)
        }
        
class GroupRequest(db.Model):
    __tablename__ = 'GroupRequest'
    GroupRequestId = db.Column(db.Integer, primary_key = True)
    GroupId = db.Column(db.Integer, db.ForeignKey('Groups.GroupId',ondelete='CASCADE'))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    CreatedAt = db.Column(db.DateTime)
    
    def get_id(self):
        return self.GroupRequestId

    def serialize(self):
        return {
            'groupRequestId': self.GroupRequestId,
            'groupId': self.GroupId,
            'clientId': self.ClientId,
            'createdAt': json.dumps(self.CreatedAt, indent=4, cls=DateTimeEncoder)
        }
    
class PostConfirm(db.Model):
    __tablename__ = 'PostConfirm'
    PostConfirmId = db.Column(db.Integer, primary_key=True)
    GroupId = db.Column(db.Integer, db.ForeignKey('Groups.GroupId',ondelete='CASCADE'))
    ClientId = db.Column(db.Integer, db.ForeignKey('Client.ClientId'))
    CreatedAt = db.Column(db.DateTime)
    Content = db.Column(db.String(500))
    Img = db.Column(db.String(500))
    
    def get_id(self):
        return self.PostConfirmId
    
    def serialize(self):
        return {
            'postConfirmId': self.PostConfirmId,
            'groupId': self.GroupId,
            'clientId': self.ClientId,
            'createdAt': json.dumps(self.CreatedAt, indent=4, cls=DateTimeEncoder),
            'content': self.Content,
            'img': self.Img
        }