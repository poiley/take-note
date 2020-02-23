from app.extensions import db
import app.models.lecture
import datetime

class Discussion(db.Model):
    __tablename__ = 'discussion'

    id          = db.Column(db.Integer, primary_key=True)
    content     = db.Column(db.String(1024), nullable=False)
    sent        = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user        = db.Column(db.String(80), nullable=False)

    lecture_id  = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    lecture     = db.relationship('Lecture', back_populates='discussion')

    def __init__(self):
        pass

    def __repr__(self):
        return "<Discussion: {}>".format(self.id)
 