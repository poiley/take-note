from app.extensions import db

class User(db.Model):
    __tablename__ = 'user'

    id          = db.Column(db.Integer(), primary_key=True)
    username    = db.Column(db.String(80), unique=True, nullable=False)
    password    = db.Column(db.String(1000), nullable=False)
    display_name= db.Column(db.String(80))
    #classes = db.Column(db.<WHAT GOES HERE?>)

    def __init__(self, username, display_name, password):
        self.username       = username
        self.display_name   = display_name
        self.password       = password
        self.classes        = []

    def __repr__(self):
        return "<User: {}>".format(self.username)
