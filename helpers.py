import requests

from models import Pokemon, SamplePokemon

# Helper function to get a db session
# def dbs(db):
#     DBSession = sessionmaker(bind=db.engine)
#     session = DBSession()
#     return session

# Initialize db with real Pokemon data
def real_data(db):
    # A better way is to get pokemon_entries list from Kanto's pokedex (pokedex/2), either way its 1-151
    for x in range(1, 10):  # TODO change to 151 when working properly
        try:
            # GET POKEAPI pokemon by id
            poke_url = f"https://pokeapi.co/api/v2/pokemon/{x}/"
            params = {"format": "json"}
            headers = {"Accept": "application/json", "Content-Type": "application/json"}
            poke_info = requests.get(poke_url, params, headers)
            # Do any data tranformation here, like sprite lookup from url
            db.session.add(Pokemon(**poke_info))
        except Exception as e:
            print(e)

        if x % 5 == 0:
            print(x, "pokemon added to the database")


# Initialize db with sample Pokemon data
def sample_data(db):

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

    # Throw some samples in for test before switching over to Pokemon model
    for pokemon in STARTERS["data"]:
        db.session.add(SamplePokemon(id=pokemon["id"], name=pokemon["name"]))
        print(pokemon["name"], "added to the database")
    # Check Pokemon model works
    db.session.add(
        Pokemon(
            id=999,
            name="Xavier",
            types=["Human"],
            shape="bipedal",
            url="https://i_dont_exist.com",
        )
    )


# def fetch_products(app):
# """Grab product listings from BestBuy."""
# endpoint = "https://api.bestbuy.com/v1/products(customerReviewAverage>=4&customerReviewCount>100&longDescription=*)"
# params = {
#     'show': "customerReviewAverage,customerReviewCount,name,sku,image,description,manufacturer,longDescription,salePrice,sku",
#     "apiKey": app.config['BEST_BUY_API_KEY'],
#     "format": "json",
#     "pageSize": 6,
#     "totalPages": 1,
#     "sort": "customerReviewAverage.dsc"}
# headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
# r = requests.get(endpoint, params=params, headers=headers)
# products = r.json()['products']
# return products
