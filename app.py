from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class index(Resource):
    def get(self):
         return "Azure Python Demo"
        
api.add_resource(index, '/index') # Route_1


