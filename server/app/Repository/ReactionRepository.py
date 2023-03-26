from app.models import Reaction
from app import db

def Create(mabaidang, manguoidung):
    reaction = Reaction(PostId = mabaidang, ClientId = manguoidung)
    db.session.add(reaction)
    db.session.commit()
    return reaction

def GetCountByPostId(mabaidang):
    return Reaction.query.filter(Reaction.PostId == mabaidang).count()

def GetAllByPostId(mabaidang):
    return Reaction.query.filter(Reaction.PostId == mabaidang).all()

def GetAllByClientId(manguoidung):
    return Reaction.query.filter(Reaction.ClientId == manguoidung).all()

def FindById(id):
    return Reaction.query.filter(Reaction.ReactionId == id).first_or_404()

def Delete(id):
    reaction = Reaction.get_id(id)
    db.session.delete(reaction)
    db.session.commit()
    return "Deleted"

def DeleteByPostId(postId):
    reactions = Reaction.query.filter(Reaction.PostId == postId).all()
    for reaction in reactions:
        db.session.delete(reaction)
    db.session.commit()
    return 'Deleted'

def DeleteByClientIdAndPostId(clientId,postId):
    reaction = Reaction.query.filter(Reaction.ClientId == clientId,Reaction.PostId == postId).first()
    db.session.delete(reaction)
    db.session.commit()
    return 'Deleted'