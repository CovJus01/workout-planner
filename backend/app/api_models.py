from .extensions import api
from flask_restx import fields

workout_model = api.model("Workout",{
    "id": fields.Integer,
    "name": fields.String,
    "user_id": fields.Integer
}) 

workout_post_model = api.model("Workout Post", {
    "name": fields.String,
    "user_id": fields.Integer
})

user_model = api.model("User", {
    "id": fields.Integer,
    "username": fields.String,
})
user_post_model = api.model("User Post", {
    "username": fields.String,
})
