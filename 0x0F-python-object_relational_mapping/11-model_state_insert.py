#!/usr/bin/python3

"""This module is a script to retrieve data from the database"""

import sys
import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    # creating the connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name))

    # Create a session to request the database
    with Session(engine) as session:
        stmt = "INSERT INTO states(name) VALUES('Louisiana')"
        session.execute(text(stmt))
        session.commit()

        stmt = "SELECT id FROM states WHERE name='Louisiana'"
        result_obj = session.execute(stmt)
        result = result_obj.first()

        print("SUCCESS")
        print(result[0])
