from .extensions import db

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.ForeignKey("user.id"))

    user = db.relationship("User", back_populates="workouts")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    workouts = db.relationship("Workout", back_populates="user")
