#!/usr/bin/python3
"""
This module defines a State class that inherits from sqlalchemy Base class
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This is the State class that will map objects from states table"""
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
