from config import app, migrate

from models import db

from helpers import *

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

def display_all_dogs():
  dogs = get_all_dogs()
  for dog in dogs:
    print(dog)

def create_new_pet():
  pet_name = get_input("What is the name of your pet? ")
  new_pet = Dog(name = pet_name)
  db.session.add(new_pet)
  db.session.commit()
  return new_pet.name

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    print("ROUTINE BUBBA")
    print("Hello!")
    display_main_menu()
    choice = get_choice()
    if choice == '1':
      print(choice)
    elif choice == '2':
      pet = create_new_pet()
      print(f"Great! Let's create a new routine for {pet}.")
    else:
      exit()