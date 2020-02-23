from app.extensions import db
from app.models.hall import Hall
from app.models.discussion import Discussion
from app.models.user import UserLectureAssociation

class Lecture(db.Model):
    __tablename__= 'lecture'

    id           = db.Column(db.Integer, primary_key=True)
    dept         = db.Column(db.String(4), nullable=False)
    course_num   = db.Column(db.Integer, nullable=False)
    title        = db.Column(db.String(50), nullable=False, unique=True)
    section      = db.Column(db.Integer, nullable=False)
    days         = db.Column(db.String(3), nullable=False)
    start        = db.Column(db.Integer, nullable=False)
    end          = db.Column(db.Integer, nullable=False)

    hall_id      = db.Column(db.Integer, db.ForeignKey('hall.id'))
    hall         = db.relationship("Hall")
    discussion   = db.relationship("Discussion", uselist=False, back_populates="lecture")
    user         = db.relationship("User", secondary=UserLectureAssociation, back_populates="lecture")

    def __init__(self, dept, course_num, title, section, days, start, end):
        self.dept       = dept
        self.course_num = course_num
        self.title      = title
        self.section    = section
        self.days       = days
        self.start      = start
        self.end        = end
    
    def __repr__(self):
        return "<Lecture: {} {} {}>".format(self.dept, self.course_num, self.section)