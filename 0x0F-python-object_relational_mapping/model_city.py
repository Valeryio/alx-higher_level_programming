#!/usr/bin/python3

""" This is the module for instanciate a simple connection with sqlalchemy
"""

from model_state import State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


"""Instanciation of the Base class that will extends the defined
mapped objects"""
Base = declarative_base()


class City(Base):
    """This is the mapped City class that have a relation to the
        simple states table in the database
    Attributes:
        @__tablename__: (class attribute)
        @id: (int), the id of the state
        @name: (str), the name of the state
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,  ForeignKey("states.id"), nullable=False)


    def __repr__(self):
        """Sets the internal representation of the class"""
        return f"({self.id}, '{self.name}')"
