from . import db

# from sqlalchemy_imageattach.entity import Image, image_attachment

# Holds the pokemon class
class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    types = db.Column(db.String(50), nullable=False)
    shape = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    # icon = db.Column(Image)

    def __repr__(self):
        return f"<Pokemon #{self.id} - {self.name}>"


class SamplePokemon(db.Model):
    __tablename__ = "sample_pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Sample Pokemon #{self.id} - {self.name}>"
