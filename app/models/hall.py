from app.extensions import db
from app.services import location

class Hall(db.Model):
    __tablename__ = 'hall'

    id      = db.Column(db.Integer(), primary_key=True)
    name    = db.Column(db.String(80), nullable = False)
    abbr    = db.Column(db.String(10), nullable = True)
    x       = db.Column(db.Float())
    y       = db.Column(db.Float())

    def __init__(self, name, abbr, x=0, y=0):
        self.name   = name
        self.abbr   = abbr
        self.x      = x
        self.y      = y

    def __repr__(self):
        return "<Hall: {}>".format(self.id)

    def json_to_database():
        halls = location.get_halls()['halls']
        print('Writing {} halls to database...'.format(len(halls)))
        for h in halls:
            try:
                hall = Hall(h['name'], h['abbr'], x=h['x'], y=h['y'])
                print('Adding Hall {}, ({}, {})'.format(hall.name, hall.x, hall.y))
                db.session.add(hall)
            except Exception as e:
                print('Error in writing halls to table -- {}'.format(e))
                print('Skipping...')
                continue

        db.session.commit()