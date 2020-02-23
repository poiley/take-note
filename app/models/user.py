from app.extensions import db

UserLectureAssociation = db.Table('userlecture_association', db.Model.metadata,
    db.Column('user_id',    db.Integer, db.ForeignKey('user.id')),
    db.Column('lecture_id', db.Integer, db.ForeignKey('lecture.id'))
)

class User(db.Model):
    __tablename__ = 'user'

    id          = db.Column(db.Integer(), primary_key=True)
    username    = db.Column(db.String(80), unique=True, nullable=False)
    password    = db.Column(db.String(1000), nullable=False)
    display_name= db.Column(db.String(80))
    lecture     = db.relationship("lecture", secondary=UserLectureAssociation)

    def __init__(self, username, display_name, password):
        self.username       = username
        self.display_name   = display_name
        self.password       = password

    def __repr__(self):
        return "<User: {}>".format(self.username)

    def get(id):
        return User.query.get(id)

    def get_lecture(self):
        return User.query.with_entities(User.lecture)
