from app.extensions import db

class Hall(db.Model):
    __tablename__ = 'hall'

    id      = db.Column(db.Integer(), primary_key=True)
    name    = db.Column(db.String(80), nullable = False)
    # tuple   = db.Column(x, y)

    def __init__(self, name, tuple):
        self.name   = name
        self.tuple  = tuple

    def __repr__(self):
        return "<Chat: {}>".format(self.id)