from flask import Flask
from flask_restplus import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from model import Base, Pokemon, SamplePokemon
from routes import getID, getName, getType
from static.constants import (
    CONVENTION,
    DB_NAME,
    sample_data,
    # SWAGGER_UI_BLUEPRINT,
    # SWAGGER_URL,
)


# Initialize Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAME
# app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

api = Api(
    app=app,
    version="1.0",
    title="MXK Kanto Pokedex",
    description="Find out information about Gen I pokemon",
)
api.add_resource(getID, "/id/<int:id>")
api.add_resource(getName, "/name/<string:name>")
api.add_resource(getType, "/type/<string:types>")

# Create SQLite db
metadata = MetaData(naming_convention=CONVENTION)
db = SQLAlchemy(app, metadata=metadata)
Base.metadata.create_all(bind=db.engine)
sample_data(db=db)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Welcome to my Pokedex API, use /swagger/ to see all the options"


# Add additional routes
import routes


if __name__ == "__main__":
    app.run(debug=True)
