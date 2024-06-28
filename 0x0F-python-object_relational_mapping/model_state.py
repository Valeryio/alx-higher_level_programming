#!/usr/bin/python3

""" This is the module for instanciate a simple connection with sqlalchemy"""

import os
import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


if __name__ == "__main__":

    os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

    def start_engine():
        """This function creates a new engine object
        Returns:
            An engine object
        """
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        return create_engine(f"mysql+pymysql://{user}:\
                            {password}@localhost:3306/{database}")

    """ Create the engine that will communicate with the SQL Database"""
    engine = start_engine()
    
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
                    nullablse=False)
        name = Column(String(128), nullable=False)

        def __repr__(self):
            """Sets the internal representation of the class"""
            return f"({self.id}, '{self.name}')"

    # Create new tables in the specified database
    Base.metadata.create_all(engine)
