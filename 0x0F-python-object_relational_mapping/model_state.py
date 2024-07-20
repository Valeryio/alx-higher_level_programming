#!/usr/bin/python3

""" This is the module for instanciate a simple connection with sqlalchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


"""Instanciation of the Base class that will extends the defined
mapped objects"""
Base = declarative_base()


class State(Base):
    """This is the mapped States class that have a relation to the
        simple states table in the database
    Attributes:
        @__tablename__: (class attribute)
        @id: (int), the id of the state
        @name: (str), the name of the state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)


    def __repr__(self):
        """Sets the internal representation of the class"""
        return f"({self.id}, '{self.name}')"
