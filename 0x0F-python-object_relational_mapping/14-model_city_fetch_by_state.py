#!/usr/bin/python3
"""
a script that display cities in state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State, City)\
                           .filter(State.id == City.state_id)\
                           .order_by(City.id).all()

    for state, city in states_cities:
        print('{}: ({}) {}'. format(state.name, city.id, city.name))
