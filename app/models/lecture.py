from app.extensions import db

class Lecture(db.Model):
    __tablename__ = 'lecture'

    id          = db.Column(db.Integer(), primary_key=True)
    dept        = db.Column(db.String(4), nullable=False)
    course_num  = db.Column(db.Integer(), nullable=False)
    section     = db.Column(db.Integer(), nullable=False)
    days        = db.Column(db.String(3), nullable=False)
    start       = db.Column(db.Integer(), nullable=False)
    end         = db.Column(db.Integer(), nullable=False)
    hall        = db.relationship("Hall", uselist=False, back_populates="lecture")
    # hall        = db.Column(x, y)
    # notes       = db.Column(x, y)
    # discussion  = db.Column(x, y)

    def __init__(self, dept, course_num, section, days, start, end):
        self.dept       = dept
        self.course_num = course_num
        self.section    = section
        self.days       = days
        self.start      = start
        self.end        = end
    
    def __repr__(self):
        return "<Lecture: {} {} {}>".format(self.dept, self.course_num, self.section)