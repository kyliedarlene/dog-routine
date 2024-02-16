from models import *

# query

def get_all_dogs():
    return db.session.query(Dog).all()

def get_all_activities():
    return db.session.query(Activity).all()

def get_activity_types():
  activities = get_all_activities()
  return sorted(set([activity.type for activity in activities]))

def get_activities_by_type(type):
    return db.session.query(Activity).filter(Activity.type == type).all()