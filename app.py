from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from config import Config

# App config and connecting
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes, models

models.Base.metadata.create_all(bind=db.engine)

# Create sample data
# Config.sample_data(db=db)
# Create actual data from PokeAPI
# Config.real_data(db=db)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Welcome to my Pokedex API"


if __name__ == "__main__":
    app.run(debug=True)
