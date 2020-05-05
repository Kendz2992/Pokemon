from flask import Blueprint

from models import Pokemon, SamplePokemon


test = Blueprint("test", __name__)
pk = Blueprint("pokemon", __name__)


@test.route("/", methods=["GET", "POST"])
def test():
    if "GET":
        return "Successful GET to endpoint"
    else:
        return "Successful POST to endpoint"


@pk.route("/id/<int:id>", methods=["GET"])
def geId(id):
    poke = SamplePokemon.query.get(id)
    return {"Pokemon": poke, "id endpoint works": id}


@pk.route("/type/<string:types>", methods=["GET"])
def getType(types):
    poke = SamplePokemon.query.filter_by(type=types).all()
    return {"Pokemon": [poke], "type endpoint works": types}


@pk.route("/name/<string:name>", methods=["GET"])
def getName(name):
    poke = SamplePokemon.query.filter_by(name=name).all()
    return {"Pokemon": [poke], "name endpoint works": name}
