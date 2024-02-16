from config import app, migrate
from models import db
from helpers import *

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    print("ROUTINE BUBBA")
    print("Hello!\n")

    dog = db.session.query(Dog).filter(Dog.name == "Bats").first()
    display_routine(dog)

    # display_main_menu()
    # choice = get_choice()
    # if choice == '1':
    #   print(choice)
    # elif choice == '2':
    #   dog = create_new_dog()
    #   print(f"Great! Let's create a new routine for {dog.name.upper()}.")
    #   create_routine(dog)
    # else:
    #   exit()