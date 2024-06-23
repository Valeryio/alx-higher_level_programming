#!/usr/bin/python3

import os
import sys
import MySQLdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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


if __name__ == "__main__":

    """
    try:
        engine = start_engine
    except Exception as ex:
        print(f"The connection to the database have failed!")
    """

    engine = start_engine()
    # Instanciation of the Base class that will extends the defined
    # mapped objects
    Base = declarative_base()

    class States(Base):
        """This is the mapped States class that have a relation to the
            simple states table in the database
        Attributes:
            @__tablename__: (class attribute)
            @id: (int), the id of the state
            @name: (str), the name of the state
        """
        __tablename__ = "states"
        id = Column(Integer, primary_key=True)
        name = Column(String)

        def __repr__(self):
            return f"({self.id}, '{self.name}')"

    # Instanciating the Session object with the right database engine
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(States).all()

    for state in all_states:
        print(state)
#    print("(", state.id, ", ", state.name, ")")

    session.close()
