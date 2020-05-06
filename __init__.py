from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# App config and connecting
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import routes
from routes import poke_bp, test_bp
import helpers

db.create_all()

# Create sample data
helpers.sample_data(db)
# Create actual data from PokeAPI
# helpers.real_data(db)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Welcome to my Pokedex API"


# Api routes
app.register_blueprint(test_bp, url_prefix="/test")
app.register_blueprint(poke_bp, url_prefix="/pokemon")


if __name__ == "__main__":
    app.run(debug=True)
