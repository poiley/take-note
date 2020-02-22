from app.extensions import db

class Notes(db.Model):
    __tablename__ = 'notes'

    id      = db.Column(db.Integer(), primary_key=True)
    # chat    = db.Column(x, y)

    def __init__(self, chat):
        self.chat = chat

    def __repr__(self):
        return "<Chat: {}>".format(self.id)