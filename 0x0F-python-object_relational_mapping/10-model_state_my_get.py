#!/usr/bin/python3
"""
A script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_id = session.query(State.id).filter(State.name==state_name
                                             ).order_by(State.id).first()
    if state_id:
        print('{:d}'.format(state_id[0]))
    else:
        print('Not found')
    session.close()
