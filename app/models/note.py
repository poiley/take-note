from app.extensions import db
import datetime

class Note(db.Model):
    __tablename__ = 'notes'

    id      = db.Column(db.Integer(), primary_key=True)
    filename= db.Column(db.String(500), unique=True, nullable=False)
    uploaded= db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, filename, uploaded=None):
        self.filename = filename
        if uploaded:
            self.uploaded = uploaded

    def __repr__(self):
        return "<Note: {}>".format(self.id)