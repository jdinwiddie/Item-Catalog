import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class CatalogItem(Base):

    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable = False)

    id = Column(Integer, primary_key = True)

    description = Column(String(250))

    price = Column(String(8))


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
        }

engine = create_engine('sqlite:///superitemcatalog.db')
Base.metadata.create_all(engine)
