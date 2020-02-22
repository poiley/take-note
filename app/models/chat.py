from app.extensions import db
import datetime

class Chat(db.Model):
    __tablename__ = 'chat'

    id          = db.Column(db.Integer(), primary_key=True)
    content     = db.Column(db.String(1024), nullable=False)
    sent        = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # user        = db.

    def __init__(self, content, user, sent=None):
        self.content  = content
        self.user     = user
        if sent:
            self.sent = sent

    def __repr__(self):
        return "<Chat: {}>".format(self.id)
