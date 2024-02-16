from config import app, migrate
from models import db
from helpers import *

from tabulate import tabulate 

def display_main_menu():
  print("1 View routine(s)")
  print("2 Create a new routine")
  print("3 Exit")

def display_routine_menu():
  print("OPTIONS")
  print("1 Update routine")
  print("2 Filter by activity type")
  print("3 View weekly summary")

def update_routine_menu():
  print("OPTIONS")
  print("1 Add an activity")
  print("2 Delete an activity")
  print("3 Add or update a comment")

def display_routines():
  dogs = get_all_dogs()
  for dog in dogs:
    print(f"{dog.id} {dog.name}")
  dog_id = input("Please enter the number of the dog you would like to see: ")
  dog = db.session.get(Dog, dog_id)
  display_week(dog)
  display_routine_menu()
  choice = get_choice()
  if choice == '1':
    update_comment()
  elif choice == '2':
    type = input("Please enter the type of activity you would like to see: ")
    display_week_filtered_by_activity_type(dog, type)
  elif choice == '3':
    print("Feature coming soon!")

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

def display_day(dog, day):
  print(day.upper())
  table = [[routine.id, routine.activity.type, routine.activity.activity, routine.comment] for routine in dog.routines if routine.day == day]
  print(tabulate(table, headers=["ID", "Type", "Activity", "Comment"], tablefmt="double-grid"))

def display_week(dog):
  for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    display_day(dog, day)

def display_week_filtered_by_activity_type(dog, type):
  table = [[routine.day, routine.activity.activity, routine.comment] for routine in dog.routines if routine.activity.type == type]
  print(tabulate(table, headers=["Day", "Activity", "Comment"], tablefmt="double-grid"))

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
  types = get_activity_types()
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

# update
      
def update_comment():
  print("Please enter the ID of the activity you would like to update:")
  choice = get_choice()
  selected_activity = db.session.get(Routine, choice)
  new_comment = input(f"Enter your new comment for {selected_activity.activity.activity}: ")
  selected_activity.comment = new_comment
  db.session.commit()

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    print("ROUTINE BUBBA")
    print("Hello!\n")    
    
    display_main_menu()
    choice = get_choice()
    if choice == '1':
      display_routines()
    elif choice == '2':
      dog = create_new_dog()
      print(f"Great! Let's create a new routine for {dog.name.upper()}.")
      create_routine(dog)
    else:
      exit()