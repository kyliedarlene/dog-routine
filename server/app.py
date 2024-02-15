from config import app, migrate

from models import db

def display_main_menu():
  print("1 View routine(s)")
  print("2 Create a new routine")
  print("3 Exit")

def get_choice():
  return input("Please enter your selection: ")

def exit():
  print("Enjoy your day with your Bubba(s)!")

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
      print(choice)
    else:
      exit()

