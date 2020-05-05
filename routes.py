from flask import Blueprint


test_bp = Blueprint("test_bp", __name__)
poke_bp = Blueprint("poke_bp", __name__)


from __init__ import db
from models import Pokemon, SamplePokemon


@test_bp.route("/x", methods=["GET", "POST"])
def test():
    if "GET":
        return "Successful GET to endpoint"
    else:
        return "Successful POST to endpoint"


# Example session connect and usage in endpoint
# session = sessionLoader()
# newEntity = Entity(name = 'John')
# session.add(newEntity)
# session.commit()
# so I could do this
# def getId(id, ds = sessionLoader())
# ds.query(SamplePokemon).get(id)


@poke_bp.route("/id/<int:id>", methods=["GET"])
def geId(id):
    poke = db.session.query(SamplePokemon).get(id)
    return {"Pokemon": poke, "id endpoint works": id}


@poke_bp.route("/name/<string:name>", methods=["GET"])
def getName(name):
    poke = db.session.query(SamplePokemon).filter_by(name=name).all()
    return {"Pokemon": poke, "name endpoint works": name}


@poke_bp.route("/type/<string:types>", methods=["GET"])
def getType(types):
    poke = db.session.query(SamplePokemon).filter_by(type=types).all()
    return {"Pokemon": poke, "type endpoint works": types}
