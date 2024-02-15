from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    print("Clearing out tables...")

    Dog.query.delete()
    Activity.query.delete()

    print("Seeding dogs table...")

    beck = Dog(name = "Beck")
    db.session.add(beck)

    bowie = Dog(name = "Bowie")
    db.session.add(bowie)

    sen = Dog(name = "Sen")
    db.session.add(sen)

    montana = Dog(name = "Montana")
    db.session.add(montana)

    willow = Dog(name = "Willow")
    db.session.add(willow)

    bats = Dog(name = "Bats")
    db.session.add(bats)

    print("Seeding activities table...")

    teeth_cleaning = Activity(
      activity = "Teeth Cleaning",
      type = "GROOMING"
    )

    brushing = Activity(
      activity = "Brushing",
      type = "GROOMING"
    )

    nail_trimming = Activity(
      activity = "Nail Trimming",
      type = "GROOMING"
    )

    walk = Activity(
      activity = "Walk",
      type = "EXERCISE"
    )

    hike = Activity(
      activity = "Hike",
      type = "EXERCISE"
    )

    dock_diving = Activity(
      activity = "Dock Diving",
      type = "EXERCISE"
    )

    skijoring = Activity(
      activity = "Skijoring",
      type = "EXERCISE"
    )

    place_work = Activity(
      activity = "Place Work",
      type = "TRAINING"
    )

    trick_practice = Activity(
      activity = "Trick Practice",
      type = "TRAINING"
    )

    new_trick = Activity(
      activity = "New Trick!",
      type = "TRAINING"
    )

    recall = Activity(
      activity = "Recall",
      type = "TRAINING"
    )

    snuffle_mats = Activity(
      activity = "Snuffle Mats",
      type = "ENRICHMENT"
    )

    nose_work = Activity(
      activity = "Nose Work",
      type = "ENRICHMENT"
    )

    db.session.add(teeth_cleaning)
    db.session.add(brushing)
    db.session.add(nail_trimming)
    db.session.add(walk)
    db.session.add(hike)
    db.session.add(dock_diving)
    db.session.add(skijoring)
    db.session.add(place_work)
    db.session.add(trick_practice)
    db.session.add(new_trick)
    db.session.add(recall)
    db.session.add(snuffle_mats)
    db.session.add(nose_work)

    db.session.commit()

    