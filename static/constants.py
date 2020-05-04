from flask_swagger_ui import get_swaggerui_blueprint

# from main import db
from model import SamplePokemon

### swagger specific ###
# SWAGGER_URL = "/swagger"
# API_URL = "/static/swagger.json"
# SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL, API_URL, config={"app_name": "MXK Pokemon API"}
# )

DB_NAME = "sqlite:///pokedex.db"
CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

### db sample data ##
STARTERS = {
    "data": [
        {"id": 1, "name": "Bulbasaur"},
        {"id": 2, "name": "Bulbasaur2"},
        {"id": 3, "name": "Bulbasaur3"},
        {"id": 4, "name": "Charmander"},
        {"id": 5, "name": "Charmander2"},
        {"id": 6, "name": "Charmander3"},
        {"id": 7, "name": "Squirtle"},
        {"id": 8, "name": "Squirtle2"},
        {"id": 9, "name": "Squirtle3"},
    ]
}

# Initialize db with sample data
def sample_data(db):
    for pokemon in STARTERS["data"]:
        db.session.add(SamplePokemon(id=pokemon["id"], name=pokemon["name"]))
    # db.session.commit()
