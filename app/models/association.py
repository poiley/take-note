from app.extensions import db, Base

UserLectureAssociation = db.Table('userlecture_association', Base.metadata,
    db.Column('user_id',    db.Integer, db.ForeignKey('user.id')),
    db.Column('lecture_id', db.Integer, db.ForeignKey('lecture.id'))
)