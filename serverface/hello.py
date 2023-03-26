from app import app
from app import db
from flask import Flask
from app.models import Client,Admin,Post,Comment,Reaction,Friend,Group,GroupMember,Message,FriendRequest,GroupRequest,PostConfirm

@app.shell_context_processor
def pro_shell_context():
    return {
        'db': db,
        'Client': Client,
        'Admin': Admin,
        'Group': Group,
        'Friend': Friend,
        'GroupMember': GroupMember,
        'Message': Message,
        'Post': Post,
        'Comment': Comment,
        'Reaction': Reaction,
        'FriendRequest': FriendRequest,
        'GroupRequest': GroupRequest,
        'PostConfirm': PostConfirm
    }
