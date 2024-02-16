from config import app, migrate
from models import db
from helpers import *

from tabulate import tabulate 

### MENUS

def display_main_menu():
  print("OPTIONS")
  print("1 View and manage routines")
  print("2 Create a new routine")
  print("3 Exit")

def view_and_manage_routines_menu():
  print("OPTIONS")
  print("1 Update routine")
  print("2 Filter by activity type")
  print("3 View weekly summary")
  print("4 Return to Main Menu")

def update_routine_menu():
  print("OPTIONS")
  print("1 Add an activity")
  print("2 Delete an activity")
  print("3 Add or update a comment")

def get_choice():
  return input("Please enter your selection: ")

### LOOPS
  
def main():
  display_main_menu()
  while True:
    choice = get_choice()
    if choice == '1':
      # view and manage routines
      view_and_manage_routines()
      break
    elif choice == '2':
      # create a new routine
      dog = create_new_dog()
      print(f"Great! Let's create a new routine for {dog.name.upper()}.")
      assign_weekly_routine(dog)
      break
    elif choice == '3':
      exit()
      break
    else:
      print("Selection must be a number between 1 and 3.")

def select_routine_by_dog():
  # print names of all dogs
  display_all_dogs()
  # get dog selection
  dog_count = len(get_all_dogs())
  while True:
    dog_id = input("Please enter the number of the dog whose routine you would like to see: ")
    try:
      dog_id = int(dog_id)
    except:
      print(f"Selection must be a number between 1 and {dog_count}.")
      continue
    if 1 <= int(dog_id) <= dog_count:
      dog = get_dog_by_id(dog_id)
      break
    else:
      print(f"Selection must be a number between 1 and {dog_count}.")
  # display selected dog's weekly routine
  display_week(dog)
  return dog

def view_and_manage_routines():
  dog = select_routine_by_dog()
  # print submenu: View and manage routines
  view_and_manage_routines_menu()
  # get menu selection
  while True:
    choice = get_choice()
    if choice == '1':
      # update routine
      update_routine()
      break
    elif choice == '2':
      # filter by activity type
      while True:
        type = input("Please enter the type of activity you would like to see: ")
        types = get_activity_types()
        if type.upper() not in types:
          print(f"Selection must be one of the following types:")
          for type in types:
            print(type)
        else:
          break
      display_week_filtered_by_activity_type(dog, type)
      view_and_manage_routines_menu()
    elif choice == '3':
      # view weekly summary
      print("View weekly summary: coming soon!")
    elif choice == '4':
      # return to main menu
      main()
      break
    else:
      print("Selection must be a number between 1 and 4.")

def update_routine():
  update_routine_menu()
  choice = get_choice()
  if choice == '1':
    # add an activity
    print("Add an activity: coming soon!")
  elif choice == '2':
    # delete an activity
    delete_routine()
  elif choice == '3':
    # add or update a comment
    update_comment()

def exit():
  print("Enjoy your week with your pups!")

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
  print(f"{dog.name.upper()}'S weekly routine!")
  for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    display_day(dog, day)

def display_week_filtered_by_activity_type(dog, type):
  print(f"{dog.name.upper()}'S {type.upper()} routine!")
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

def autofill_weekly_routine(dog):
  model_day = get_routine_by_dog(dog.id)
  for day in ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    for routine in model_day:
      create_new_routine(dog, routine.activity_id, day)

def assign_weekly_routine(dog):
  assign_daily_routine(dog, "Monday")
  print(f"{dog.name}'s MONDAY routine is complete!")
  print(f"Would you like to model the rest of the week after {dog.name}'s MONDAY routine? You'll be able to fine-tune each day's activities later.")
  print(f"1 Autofill {dog.name}'s weekly schedule")
  print(f"2 Fill out each day manually")
  selection = get_choice()
  if selection == '1':
    autofill_weekly_routine(dog)
    # display_week(dog)
  elif selection == '2':
    for day in ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
      assign_daily_routine(dog, day)

### UPDATE
      
def update_comment():
  choice = input("Please enter the ID of the activity you would like to update: ")
  selected_activity = db.session.get(Routine, choice)
  new_comment = input(f"Enter your new comment for {selected_activity.activity.activity}: ")
  selected_activity.comment = new_comment
  db.session.commit()

### DELETE
  
def delete_routine():
  choice = input("Please enter the number of the activity you would like to delete: ")
  selected_activity = db.session.get(Routine, choice)
  choice = input(f"Are you sure you want to delete {selected_activity.activity.activity} in {selected_activity.dog.name.upper()}'S {selected_activity.day} schedule? This cannot be undone. (Y/N): ")
  if choice == 'N':
    return
  elif choice == 'Y':
    db.session.delete(selected_activity)
    db.session.commit()
    print(f"{selected_activity.activity.activity} has been deleted.")

#### RUN APP

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    
    print("ROUTINE BUBBA")
    print("Hello!\n")    
    
    main()