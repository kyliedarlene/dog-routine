from models import *

def get_all_dogs():
    return db.session.query(Dog).all()