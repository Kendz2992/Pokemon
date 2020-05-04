from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy_imageattach.entity import Image, image_attachment

Base = declarative_base()

# Holds the pokemon class
class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    types = Column(String(50), nullable=False)
    shape = Column(String(100), nullable=False)
    url = Column(String(150), nullable=False)
    # icon = Column(Image)

    def __repr__(self):
        return f"<Pokemon #{self.id} - {self.name}>"


class SamplePokemon(Base):
    __tablename__ = "sample_pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Sample Pokemon #{self.id} - {self.name}>"
