from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from src.get import createJson

app = Flask(__name__)
api = Api(app)

class Coordinates(Resource):
    def get(self):
        data = createJson() # string json que o fonfon ta criando

        return {'data': data }, 200

api.add_resource(Coordinates, '/coordinates')


if __name__ == '__main__':
    app.run()