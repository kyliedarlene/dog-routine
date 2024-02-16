from config import db

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique = True)

    routines = db.relationship("Routine", backref = "dog")

    def __repr__(self):
        return f"Dog: {self.name}"

class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer(), primary_key=True)
    activity = db.Column(db.String(), unique = True)
    type = db.Column(db.String())

    routines = db.relationship("Routine", backref = "activity")

    def __repr__(self):
        return f"Activity: {self.activity} Type: {self.type}"
    
class Routine(db.Model):
    __tablename__ = "routines"

    id = db.Column(db.Integer(), primary_key=True)
    dog_id = db.Column(db.Integer(), db.ForeignKey('dogs.id'))
    activity_id = db.Column(db.Integer(), db.ForeignKey('activities.id'))
    day = db.Column(db.String())
    comment = db.Column(db.String())

    def __repr__(self):
        return f"{self.day.upper()} | {self.activity.type} | {self.activity.activity}"