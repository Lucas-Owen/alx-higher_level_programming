#!/usr/bin/python3
"""
This module defines a City class that inherits from sqlalchemy Base class
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """This is the City class that will map objects from cities table"""
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
    name = Column('name', String(128), nullable=False)
