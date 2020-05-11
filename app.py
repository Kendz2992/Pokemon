from dataclasses import dataclass
from flask import Flask, json, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# App config and connecting
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Models
@dataclass
class Pokemon(db.Model):
    # __tablename__ = "sample_pokemon"

    order = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __repr__(self):
        return f"<Sample Pokemon #{self.num} - {self.name}>"


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Welcome to my Pokedex API"


@app.route("/poke")
def allPoke():
    q = Pokemon.query.all()
    # dq = [poke.__dict__ for poke in q]
    # jq = jsonify(dq)
    return jsonify(q)


@app.route("/id/<int:pid>", methods=["GET"])
def geId(pid):
    poke = Pokemon.query.filter_by(num=pid)
    # Would eventually display the results of the endpoint in the template html
    # return render_template("users.jinja2", users=User.query.all(), title="Show Pokemon")
    return {"Pokemon": jsonify(poke), "id endpoint works": pid}


@app.route("/type/<string:types>", methods=["GET"])
def getType(types):
    poke = Pokemon.query.filter_by(type=types).all()
    # Same return_template as above
    return {"Pokemon": jsonify(poke), "type endpoint works": types}


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == "__main__":
    # Create tables
    db.create_all()
    print(Pokemon.query.all())

    # Create sample data
    sample_data = [Pokemon(num=1, name="a"), Pokemon(num=2, name="b")]

    # Save info
    # db.session.add_all(sample_data)
    for thing in sample_data:
        db.session.add(thing)
    db.session.commit()
    print(Pokemon.query.all())

    # db.session.close()

    # Start app
    app.run(debug=True)
