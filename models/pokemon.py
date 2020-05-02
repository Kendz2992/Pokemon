from sqlalchemy import Column, Integer, String, Array, Model
from sqlalchemy_imageattach.entity import Image, image_attachment

# Hold pokemon class
class Pokemon(Model):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    types = Column(Array, nullable=False)
    shape = Column(String(100), nullable=False)
    url = Column(String(150), nullable=False)
    icon = Column(Image, nullable=False)

    def __repr__(self):
        return f"<Pokemon #{self.id} - {self.name}>"
