from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import uvicorn

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////MXK/pokemon_challenge.db"

### swagger specific ###
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "MXK Pokemon API"}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

# TODO create engine/session for app
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
    # uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info", reload=True)
