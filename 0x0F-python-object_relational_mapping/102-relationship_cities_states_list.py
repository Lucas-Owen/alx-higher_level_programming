#!/usr/bin/python3
"""
This script demonstrates one to many relationship
It lists all State objects, and corresponding City objects
from the database hbtn_0e_101_usa
"""


if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id):
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))
    session.close()
