#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

"""
user_place = Table('User_place',
                   Base.metadata,
                   Column('User_ID', String(60), ForeignKey('users.id'),
                   nullable=False),
                   Column('Place_ID', String(60), ForeignKey('places.id'),
                   nullable=False)
                   )


place_city = Table('Place_city',
                   Base.metadata,
                   Column('Place_ID', String(60), ForeignKey('places.id'),
                   nullable=False),
                   Column('City_ID', String(60), ForeignKey('cities.id'),
                   nullable=False)
                   )
"""


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if not os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    else:
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
