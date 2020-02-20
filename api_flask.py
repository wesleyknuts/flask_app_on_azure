from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
# from flask.ext.jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

class index(Resource):
    def get(self):
         return "Azure Python Demo"
        

api.add_resource(index, '/index') # Route_1



if __name__ == '__main__':
     app.run(port='5002')