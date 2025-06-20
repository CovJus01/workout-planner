from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


# Workout Endpoint
@app.get("/workout/<workout_name>")
def get_workout(workout_name):
    return  {"workout": workout_name}, 200


@app.post("/workout/<workout_name>")
def post_workout(workout_name):
    return  {"workout": workout_name}, 200
