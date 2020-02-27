from app.extensions import db
from app.models.hall import Hall
from app.models.discussion import Discussion
from app.models.user import UserLectureAssociation
from app.models.hall import Hall
from app.services import schedule

class Lecture(db.Model):
    __tablename__= 'lecture'

    id           = db.Column(db.Integer, primary_key=True)
    dept         = db.Column(db.String(10), nullable=False)
    course_num   = db.Column(db.Integer, nullable=False)
    title        = db.Column(db.String(50), nullable=False)
    section      = db.Column(db.Integer, nullable=False)
    days         = db.Column(db.String(10), nullable=False)
    start        = db.Column(db.Integer, nullable=False)
    end          = db.Column(db.Integer, nullable=False)
    professor    = db.Column(db.String(50), nullable=True)

    hall_id      = db.Column(db.Integer, db.ForeignKey('hall.id'))
    hall         = db.relationship("Hall")
    discussion   = db.relationship("Discussion", uselist=False, back_populates="lecture")
    user         = db.relationship("User", secondary=UserLectureAssociation, back_populates="lecture")

    def __init__(self, dept, course_num, title, section, days, start, end, professor):
        self.dept       = dept
        self.course_num = course_num
        self.title      = title
        self.section    = section
        self.days       = days
        self.start      = start
        self.end        = end
        self.professor  = professor
    
    def __repr__(self):
        return "<Lecture: {} {} {}>".format(self.dept, self.course_num, self.section)
    
    def get(id):
        return Lecture.query.get(id)
    
    def json_to_database():
        classes = schedule.get_classes()['classes']
        print('Writing {} lectures to database...'.format(len(classes)))
        for c in classes:
            try:
                lect = Lecture(c['dept'], c['course_num'], c['title'], c['section'], c['days'], c['start'], c['end'], c['professor'])

                lect.hall = Hall.query.filter(Hall.abbr == c['hall'].split(' ')[0]).first()

                print('Adding Lecture {} {} {}, starts at {}, taught by {}'.format(lect.dept, lect.course_num, lect.title, lect.start, lect.professor))
                db.session.add(lect)
            except Exception as e:
                print('Error in writing lectures to table -- {}'.format(e))
                print('Skipping...')
                continue
        db.session.commit()
        
