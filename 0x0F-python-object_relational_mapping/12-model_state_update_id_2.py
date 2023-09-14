#!/usr/bin/python3
"""
A script that changes the name of the State where id = 2 to New Mexico
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.id==2).update(
        {State.name: 'New Mexico'})
    session.commit()
    for state in session.query(State):
        print("{:d}: {:s}".format(state.id, state.name))
    session.close()
