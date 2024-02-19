#!/usr/bin/python3
"""
A script that prints the State object with the name passed as
argument from a database
"""

from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
