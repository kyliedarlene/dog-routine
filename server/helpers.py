from models import *

def get_all_dogs():
    return db.session.query(Dog).all()

def get_dog_by_id(id):
    return db.session.get(Dog, id)

def get_all_activities():
    return db.session.query(Activity).all()

def get_activity_types():
  activities = get_all_activities()
  return sorted(set([activity.type for activity in activities]))

def get_activities_by_type(type):
    return db.session.query(Activity).filter(Activity.type == type).all()

def get_routine_by_pet(dog_id):
    return db.session.query(Routine).filter(Routine.dog_id == dog_id).all()