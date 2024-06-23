#!/usr/bin/python3

import os
import sys
import MySQLdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/{database}")
Base = declarative_base()


class States(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"({self.id}, '{self.name}')"

Session = sessionmaker(bind=engine)
session = Session()

all_states = session.query(States).all()

for state in all_states:
    print(state)
#    print("(", state.id, ", ", state.name, ")")

session.close()
