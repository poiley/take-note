from app.extensions import db

class Lecture(db.Model):
    __tablename__ = 'lecture'

    id          = db.Column(db.Integer(), primary_key=True)
    dept        = db.Column(db.String(), nullable = False)
    course_num  = db.Column(db.Integer(), nullable = False)
    section     = db.Column(db.Integer(), nullable = False)
    # days        = db.Column(x, y)
    # tuple       = db.Column(x, y)
    # hall        = db.Column(x, y)
    # notes       = db.Column(x, y)
    # discussion  = db.Column(x, y)

    def __init__(self, dept, course_num, section, days, tuple, hall, notes, discussion):
        self.dept           = dept
        self.course_num     = course_num
        self.section        = section
        self.days           = days
        self.tuple          = tuple
        self.hall           = hall
        self.notes          = notes
        self.discussion     = discussion
    
    def __repr__(self):
        return "<Chat: {}>".format(self.id)