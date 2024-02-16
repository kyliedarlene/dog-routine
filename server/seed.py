from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    print("Clearing out tables...")

    Dog.query.delete()
    Activity.query.delete()
    Routine.query.delete()

    print("Seeding dogs table...")

    beck = Dog(name = "Beck")
    db.session.add(beck)

    bowie = Dog(name = "Bowie")
    db.session.add(bowie)

    print("Seeding activities table...")

    teeth_cleaning = Activity(
      activity = "Teeth Cleaning",
      type = "GROOMING"
    )
    db.session.add(teeth_cleaning)

    brushing = Activity(
      activity = "Brushing",
      type = "GROOMING"
    )
    db.session.add(brushing)

    bath = Activity(
      activity = "Bath",
      type = "GROOMING"
    )
    db.session.add(bath)

    nail_trimming = Activity(
      activity = "Nail Trimming",
      type = "GROOMING"
    )
    db.session.add(nail_trimming)

    walk = Activity(
      activity = "Walk",
      type = "EXERCISE"
    )
    db.session.add(walk)

    hike = Activity(
      activity = "Hike",
      type = "EXERCISE"
    )
    db.session.add(hike)

    run = Activity(
      activity = "Run",
      type = "EXERCISE"
    )
    db.session.add(run)

    bike_ride = Activity(
      activity = "Bike Ride",
      type = "EXERCISE"
    )
    db.session.add(bike_ride)

    fetch = Activity(
      activity = "Fetch",
      type = "EXERCISE"
    )
    db.session.add(fetch)

    dock_diving = Activity(
      activity = "Dock Diving",
      type = "EXERCISE"
    )
    db.session.add(dock_diving)

    skijoring = Activity(
      activity = "Skijoring",
      type = "EXERCISE"
    )
    db.session.add(skijoring)

    place_work = Activity(
      activity = "Place Work",
      type = "TRAINING"
    )
    db.session.add(place_work)

    trick_practice = Activity(
      activity = "Trick Practice",
      type = "TRAINING"
    )
    db.session.add(trick_practice)

    new_trick = Activity(
      activity = "New Trick!",
      type = "TRAINING"
    )
    db.session.add(new_trick)

    recall = Activity(
      activity = "Recall",
      type = "TRAINING"
    )
    db.session.add(recall)

    puzzle_toy = Activity(
      activity = "Puzzle Toy",
      type = "ENRICHMENT"
    )
    db.session.add(puzzle_toy)

    nose_work = Activity(
      activity = "Nose Work",
      type = "ENRICHMENT"
    )
    db.session.add(nose_work)

    agility = Activity(
      activity = "Agility",
      type = "ENRICHMENT"
    )
    db.session.add(agility)

    db.session.commit()

    print("Seeding routines table...")

    r1 = Routine(
      dog_id = 1,
      activity_id = 1,
      day = "Monday",
      comment = ""
    )
    db.session.add(r1)

    r2 = Routine(
      dog_id = 1,
      activity_id = 6,
      day = "Monday",
      comment = "Pattee Canyon"
    )
    db.session.add(r2)

    r3 = Routine(
      dog_id = 1,
      activity_id = 13,
      day = "Monday",
      comment = "practicing figure 8"
    )
    db.session.add(r3)

    r4 = Routine(
      dog_id = 1,
      activity_id = 16,
      day = "Monday",
      comment = "stuffed Kong"
    )
    db.session.add(r4)

    r5 = Routine(
      dog_id = 1,
      activity_id = 2,
      day = "Tuesday",
      comment = ""
    )
    db.session.add(r5)

    r6 = Routine(
      dog_id = 1,
      activity_id = 10,
      day = "Tuesday",
      comment = "8am appointment @ DogMode"
    )
    db.session.add(r6)

    r7 = Routine(
      dog_id = 1,
      activity_id = 15,
      day = "Tuesday",
      comment = "practice by skate park"
    )
    db.session.add(r7)

    r8 = Routine(
      dog_id = 1,
      activity_id = 17,
      day = "Tuesday",
      comment = "foraging for lunch"
    )
    db.session.add(r8)

    r9 = Routine(
      dog_id = 1,
      activity_id = 3,
      day = "Wednesday",
      comment = ""
    )
    db.session.add(r9)

    r10 = Routine(
      dog_id = 1,
      activity_id = 8,
      day = "Wednesday",
      comment = "Blue Mountain backside trail"
    )
    db.session.add(r10)

    r11 = Routine(
      dog_id = 1,
      activity_id = 14,
      day = "Wednesday",
      comment = "learning sit pretty"
    )
    db.session.add(r11)

    r12 = Routine(
      dog_id = 1,
      activity_id = 18,
      day = "Wednesday",
      comment = ""
    )
    db.session.add(r12)

    r13 = Routine(
      dog_id = 1,
      activity_id = 4,
      day = "Thursday",
      comment = ""
    )
    db.session.add(r13)

    r14 = Routine(
      dog_id = 1,
      activity_id = 5,
      day = "Thursday",
      comment = ""
    )
    db.session.add(r14)

    r15 = Routine(
      dog_id = 1,
      activity_id = 12,
      day = "Thursday",
      comment = ""
    )
    db.session.add(r15)

    r16 = Routine(
      dog_id = 1,
      activity_id = 16,
      day = "Thursday",
      comment = "lick mat"
    )
    db.session.add(r16)

    r17 = Routine(
      dog_id = 1,
      activity_id = 1,
      day = "Friday",
      comment = ""
    )
    db.session.add(r17)

    r18 = Routine(
      dog_id = 1,
      activity_id = 9,
      day = "Friday",
      comment = ""
    )
    db.session.add(r18)

    r19 = Routine(
      dog_id = 1,
      activity_id = 13,
      day = "Thursday",
      comment = "practicing figure 8"
    )
    db.session.add(r19)

    r20 = Routine(
      dog_id = 1,
      activity_id = 16,
      day = "Friday",
      comment = "rolly ball"
    )
    db.session.add(r20)

    r21 = Routine(
      dog_id = 1,
      activity_id = 2,
      day = "Saturday",
      comment = ""
    )
    db.session.add(r21)

    r22 = Routine(
      dog_id = 1,
      activity_id = 6,
      day = "Saturday",
      comment = "Marshall Mountain"
    )
    db.session.add(r22)

    r23 = Routine(
      dog_id = 1,
      activity_id = 12,
      day = "Saturday",
      comment = ""
    )
    db.session.add(r23)

    r24 = Routine(
      dog_id = 1,
      activity_id = 16,
      day = "Saturday",
      comment = "stuffed Kong"
    )
    db.session.add(r24)

    r25 = Routine(
      dog_id = 1,
      activity_id = 1,
      day = "Sunday",
      comment = ""
    )
    db.session.add(r25)

    r26 = Routine(
      dog_id = 1,
      activity_id = 7,
      day = "Sunday",
      comment = ""
    )
    db.session.add(r26)

    r27 = Routine(
      dog_id = 1,
      activity_id = 12,
      day = "Sunday",
      comment = ""
    )
    db.session.add(r27)

    r28 = Routine(
      dog_id = 1,
      activity_id = 17,
      day = "Sunday",
      comment = ""
    )
    db.session.add(r28)

    db.session.commit()