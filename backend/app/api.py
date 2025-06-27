from flask_restx import Resource, Namespace
from .api_models import workout_model, workout_post_model, user_post_model, user_model
from .extensions import db
from .models import Workout, User

ns = Namespace("api")

@ns.route("/workouts")
class WorkoutsAPI(Resource):

    @ns.marshal_list_with(workout_model)
    def get(self):
        return Workout.query.all(), 200

    @ns.expect(workout_post_model)
    @ns.marshal_with(workout_model)
    def post(self):
        workout = Workout(name=ns.payload["name"], user_id=ns.payload["user_id"])
        db.session.add(workout)
        db.session.commit()

        return workout, 201


@ns.route("/user")
class UserAPI(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        return User.query.all(), 200

    @ns.expect(user_post_model)
    @ns.marshal_with(user_model)
    def post(self):
        user = User(username=ns.payload["username"])
        db.session.add(user)
        db.session.commit()

        return user, 201
