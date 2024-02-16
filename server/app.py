from config import app, migrate
from models import db
from helpers import *

from tabulate import tabulate 

### MENUS

def display_main_menu():
  print("1 View and manage routines")
  print("2 Create a new routine")
  print("3 Exit")

def view_and_manage_routines_menu():
  print("OPTIONS")
  print("1 Update routine")
  print("2 Filter by activity type")
  print("3 View weekly summary")

def update_routine_menu():
  print("OPTIONS")
  print("1 Add an activity")
  print("2 Delete an activity")
  print("3 Add or update a comment")

def get_choice():
  return input("Please enter your selection: ")

### LOOPS & PATHS
  
def view_and_manage_routines():
  display_all_dogs()
  dog_id = input("Please enter the number of the dog whose routine you would like to see: ")
  dog = get_dog_by_id(dog_id)
  display_week(dog)
  view_and_manage_routines_menu()
  choice = get_choice()
  if choice == '1':
    update_routine()
  elif choice == '2':
    type = input("Please enter the type of activity you would like to see: ")
    display_week_filtered_by_activity_type(dog, type)
  elif choice == '3':
    print("Feature coming soon!")

def update_routine():
  update_routine_menu()
  choice = get_choice()
  if choice == '1':
    print("Add an activity (NOT BUILT)")
  elif choice == '2':
    print("Delete an activity (NOT BUILT)")
  elif choice == '3':
    update_comment()

def exit():
  print("Enjoy your day with your Bubba(s)!")

### READ 
  
## dogs

def display_all_dogs():
  dogs = get_all_dogs()
  for dog in dogs:
    print(f"{dog.id} {dog.name}")

## activities
    
def display_activities_by_type(type):
  activities = get_activities_by_type(type)
  for activity in activities:
    print(f"{activity.id} {activity.activity}")

## routines
    
def display_day(dog, day):
  print(day.upper())
  table = [
    [routine.id, routine.activity.type, routine.activity.activity, routine.comment] 
    for routine in dog.routines 
    if routine.day == day
  ]
  print(tabulate(table, headers=["ID", "Type", "Activity", "Comment"], tablefmt="double-grid"))

def display_week(dog):
  for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    display_day(dog, day)

def display_week_filtered_by_activity_type(dog, type):
  table = [
    [routine.day, routine.activity.activity, routine.comment] 
    for routine in dog.routines 
    if routine.activity.type == type
  ]
  print(tabulate(table, headers=["Day", "Activity", "Comment"], tablefmt="double-grid"))

### CREATE

## dogs
  
def create_new_dog():
  dog_name = input("What is the name of your dog? ")
  new_dog = Dog(name = dog_name)
  db.session.add(new_dog)
  db.session.commit()
  return new_dog

## routines 

def create_new_routine(dog, activity, day):
  new_routine = Routine(
    dog_id = dog.id,
    activity_id = activity,
    day = day,
    comment = ""
  )
  db.session.add(new_routine)
  db.session.commit()
    
def assign_daily_routine(dog, day):
  types = get_activity_types()
  for type in types:
    print(f"Please add any {type} activities that you'll be doing with {dog.name.upper()} on {day.upper()}.")
    print("When you're finished, press ENTER to continue.")
    display_activities_by_type(type)
    selection = None
    while selection != "":
      selection = input("Add an activity: ")
      if selection == "":
        break
      else:
        create_new_routine(dog, selection, day)

def assign_weekly_routine(dog):
  assign_daily_routine(dog, "Monday")
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
      assign_daily_routine(dog, day)

### UPDATE
      
def update_comment():
  print("Please enter the ID of the activity you would like to update:")
  choice = get_choice()
  selected_activity = db.session.get(Routine, choice)
  new_comment = input(f"Enter your new comment for {selected_activity.activity.activity}: ")
  selected_activity.comment = new_comment
  db.session.commit()

#### RUN APP

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    print("ROUTINE BUBBA")
    print("Hello!\n")    
    
    display_main_menu()
    choice = get_choice()
    if choice == '1':
      view_and_manage_routines()
    elif choice == '2':
      dog = create_new_dog()
      print(f"Great! Let's create a new routine for {dog.name.upper()}.")
      assign_weekly_routine(dog)
    else:
      exit()