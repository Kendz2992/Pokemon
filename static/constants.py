from flask_swagger_ui import get_swaggerui_blueprint

### swagger specific ###
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "MXK Pokemon API"}
)

DB_NAME = "sqlite:///pokedex.db"
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
