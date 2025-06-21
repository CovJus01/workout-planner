import json
from flask import Flask, request
from flask_restx import Resource, Api, fields
from db import get_db, close_db

app = Flask(__name__)
api = Api(app)

workout = api.namespace('workout', description="Where all workout requests are handled")


workout_model = api.model('Workout',{
    'author_id': fields.Integer(required=True, description='Author ID'),
    'title': fields.String(required=True, description='Workout Title'),
    'desc': fields.String(required=True, description='Workout body'),
})

@workout.route('/')
class Workout(Resource):
    def get(self):
        """ Get a workout """
            
        db = get_db()

        try:
            response = db.execute('Select * from workout').fetchone()
        except OSError as e:
            workout.logger.error(str(e))

        workout.logger.info(response)

        close_db()
        response = dict(response)
        response = json.dumps(response)

        return response, 200

    @workout.expect(workout_model, validate=True)
    def post(self):
        """ Create a workout """
        workout_data = request.get_json() 
        db = get_db()

        try:
            db.execute(
                'INSERT INTO workout (author_id, title, desc) VALUES (:author_id,:title,:desc)',
                workout_data
            )
        except OSError as e:
            workout.logger.error(str(e))
        close_db()

        return workout_data, 200


if __name__ == '__main__':
    app.run(debug=True)
