#!/usr/bin/python3

import os
import MySQLdb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

engine = create_engine("mysql+pymysql://root:Val_Ery28!@localhost:3306/hbtn_0e_0_usa")
Base = declarative_base()


class States(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

all_states = session.query(States).all()

for state in all_states:
    print(state.id, " : ", state.name)

session.close()
