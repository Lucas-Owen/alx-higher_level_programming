#!/usr/bin/python3
"""
This script demonstrates one to many relationship
It creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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
    state = State(name="California", cities=[])
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)
    session.commit()
    session.delete(state)
    session.close()
