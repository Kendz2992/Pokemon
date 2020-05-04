# Pokemon

Pokedex Programming Challenge

Using Flask, Python3, SQLAlchemy ORM and Alembic we would like you to create a simple table utilizing an API, The application should fulfill the basic requirements below. The source code must be placed in a public repo on Github.

- Utilizing the Pokedex API at ​https://pokeapi.co/​ Create a table that displays the Kanto pokedex pokemon in order of ID by default
- Allow Search queries to search for pokemon based on name, ie 'char' should result in Charmander, Charmeleon, and Charizard.
- Add show option for each pokemon which will present detailed information on pokemon such as Name, ID, Capture rate as a percentage, Types, and what shape the pokemon has(ex. quadruped for Venosaur)
- Add an ability to filter the table by type, ie fire or flying etc
- The table should have an option to export to JSON, CSV, or XML
- Table has icon for each pokemon, use front default. 'Show' page should show the
sprite as well.
- Deploy a sample of the application to a free instance of AWS or Heroku


# Using a virtual environment
## Bash commands
- `cd Pokedex`
- `python3 -m venv venv/`
- `source venv/bin/activate`
Bash should now have `(venv)` prefix
- `pip install -r requirements.txt`
- `export FLASK_APP=Pokedex`
- `flask run`
You should be able to follow to the localhost url to view this project
