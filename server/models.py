from config import db

class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique = True)

    def __repr__(self):
        return f"Dog: {self.name}"

class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer(), primary_key=True)
    activity = db.Column(db.String(), unique = True)
    type = db.Column(db.String())

    def __repr__(self):
        return f"Activity: {self.activity} Type: {self.type}"