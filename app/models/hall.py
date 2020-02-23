from app.extensions import db

class Hall(db.Model):
    __tablename__ = 'hall'

    id      = db.Column(db.Integer(), primary_key=True)
    name    = db.Column(db.String(80), nullable = False)
    x       = db.Column(db.Float())
    y       = db.Column(db.Float())

    def __init__(self, name, x=0, y=0):
        self.name   = name
        self.x      = x
        self.y      = y

    def __repr__(self):
        return "<Hall: {}>".format(self.id)