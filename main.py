from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import Base, Pokemon, SamplePokemon
from static.constants import DB_NAME, SWAGGER_UI_BLUEPRINT, SWAGGER_URL


# Initialize Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAME
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Create SQLite db
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Welcome to my Pokedex API, use /swagger/ to see all the options"


if __name__ == "__main__":
    Base.metadata.create_all(bind=db.engine)
    app.run(debug=True)
