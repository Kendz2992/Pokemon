from flask_restplus import Resource

# from main import db
from model import Pokemon, SamplePokemon


class MainClass(Resource):
    def get(self):
        return {"status": "Got new data"}

    def post(self):
        return {"status": "Posted new data"}


class getID(Resource):
    def get(self, id):
        return {"id endpoint works": id}


class getName(Resource):
    def get(self, name):
        return {"name endpoint works": name}


class getType(Resource):
    def get(self, types):
        return {"type endpoint works": types}
