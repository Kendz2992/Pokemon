# Hit Pokemon API to get all pokemon
# Utilizing the Pokedex API at ​https://pokeapi.co/​
# GET http://pokeapi.co/api/v2/pokemon
# sort by Kanto region (ids thru 151)before committing to db

# Add all Kanto pokemon to db
# for poke in listing:
# Pokemon.create(db, **poke)
# db.commit()
# db is initialized with pokemon.
# All endpoints are internal, feeding off populated db

# Old crud
# from sqlalchemy.ext.declarative import declarative_base

# from main import db
# from models import Pokemon, SamplePokemon
# from sample_data import STARTERS


# def real_setup():
# Initialize real data
# for id in range(0,151):
# Hit PokeAPi for pokemon with id
# TODO
# Make a poke dict
# TODO
# Create a Pokemon record from dict
# db.session.add(Pokemon(**dict))
# db.session.add(
#     Pokemon(
#         id=999,
#         name="Xavier",
#         types=["Human", "Male"],
#         shape="bipedal",
#         url="https://i_dont_exist.com",
#     )
# )
# db.session.commit()


# def sample_setup():
#     # Initialize sample data
#     for pokemon in STARTERS["data"]:
#         db.session.add(SamplePokemon(id=pokemon["id"], name=pokemon["name"]))
#     db.session.commit()
