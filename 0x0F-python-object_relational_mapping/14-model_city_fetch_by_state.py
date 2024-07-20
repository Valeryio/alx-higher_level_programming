#!/usr/bin/python3

"""This module is a script to retrieve data from the database"""

import sys
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    # creating the connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name))

    # Create a session to request the database
    with Session(engine) as session:
        stmt = "SELECT states.name, cities.id, cities.name FROM cities INNER\
                JOIN states ON states.id=cities.state_id"
        result_obj = session.execute(text(stmt))
        result = result_obj.fetchall()

    for i in result:
        print(i[0] + ": (" + str(i[1]) + ") " + i[2])
