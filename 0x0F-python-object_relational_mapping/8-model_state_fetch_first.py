#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print('{:d}: {:s}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
