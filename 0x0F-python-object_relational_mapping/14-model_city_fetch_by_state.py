#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine, delete)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State.name, City.id, City.name).join(
        State).filter(City.state_id == State.id).order_by(City.id)
    for state_name, city_id, city_name in result:
        print("{:s}: ({:d}) {:s}".format(state_name, city_id, city_name))
    session.close()
