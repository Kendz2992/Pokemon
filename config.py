import requests

from models import Pokemon, SamplePokemon


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONVENTION = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    # Initialize db with real Pokemon data
    def real_data(db):
        for x in range(1, 10):  # TODO change to 151 when working properly
            try:
                # pokemon = GET POKEAPI url by id x
                # db.session.add(Pokemon(**pokemon))
                pass
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
                types=["Human", "Male"],
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
