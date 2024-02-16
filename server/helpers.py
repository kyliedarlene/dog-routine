from models import *

# query

def get_all_dogs():
    return db.session.query(Dog).all()

def get_all_activities():
    return db.session.query(Activity).all()

def get_activities_by_type(type):
    return db.session.query(Activity).filter(Activity.type == type).all()

def display_main_menu():
  print("1 View routine(s)")
  print("2 Create a new routine")
  print("3 Exit")

# inputs

def get_choice():
  return input("Please enter your selection: ")

def get_input(str):
  return input(str)

def exit():
  print("Enjoy your day with your Bubba(s)!")

# Read
  
def display_all_dogs():
  dogs = get_all_dogs()
  for dog in dogs:
    print(dog)

def display_routine(dog):
  pass

# Create

def create_new_dog():
  dog_name = get_input("What is the name of your dog? ")
  new_dog = Dog(name = dog_name)
  db.session.add(new_dog)
  db.session.commit()
  return new_dog

def add_routines_by_type(type, dog, day):
  print(f"Please add any {type} activities that you'll be doing with {dog.name.upper()} on {day.upper()}.")
  print("When you're finished, press ENTER to continue.")
  activities = get_activities_by_type(type)
  for activity in activities:
    print(f"{activity.id} {activity.activity}")
  selection = None
  while selection != "":
    selection = input("Add an activity: ")
    if selection == "":
      break
    else: 
      new_routine = Routine(
        dog_id = dog.id,
        activity_id = selection,
        day = day,
        comment = ""
      )
      db.session.add(new_routine)
      db.session.commit()

def create_day(dog, day):
  activities = get_all_activities()
  types = sorted(set([activity.type for activity in activities]))
  for type in types:
    add_routines_by_type(type, dog, day)

def create_routine(dog):
  create_day(dog, "Monday")
  print(f"{dog.name}'s MONDAY routine is complete!")
  print(f"Would you like to model the rest of the week after {dog.name}'s MONDAY routine? You'll be able to fine-tune each day's activities later.")
  print(f"1 Autofill {dog.name}'s weekly schedule")
  print(f"2 Fill out each day manually")
  selection = get_choice()
  print(f"Selection: {selection}")
  if selection == '1':
    print("Autofill")
  elif selection == '2':
    for day in ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
      create_day(dog, day)