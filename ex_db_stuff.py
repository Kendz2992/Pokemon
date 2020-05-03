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


# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("sqlite:////MXK/pokemon_challenge.db", convert_unicode=True)
# db_session = scoped_session(
#     sessionmaker(autocommit=False, autoflush=False, bind=engine)
# )
# Base = declarative_base()
# Base.query = db_session.query_property()


# def init_db():
#     from models.pokemon import Pokemon
#     from .setup_db import init_data

#     Base.metadata.create_all(bind=engine)
