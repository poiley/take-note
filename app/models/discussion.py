from app.extensions import db

class Discussion(db.Model):
    __tablename__ = 'discussion'

    id          = db.Column(db.Integer(), primary_key=True)
    #chats

    def __init__(self, chats=None):
        if chats:
            self.chat = chats

    def __repr__(self):
        return "<Discussion: {}>".format(self.id)
