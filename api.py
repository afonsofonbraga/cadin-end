from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from get import createJson

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
class Coordinates(Resource):
    def get(self):
        data = createJson() # string json que o fonfon ta criando

        return {'data': data }, 200,\
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods' : 'PUT,GET' }

api.add_resource(Coordinates, '/coordinates')


if __name__ == '__main__':
    app.run()
