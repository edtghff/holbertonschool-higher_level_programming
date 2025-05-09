#!/usr/bin/python3

"""Lists all State objects from the database hbtn_0e_6_usa that contain the letter 'a'."""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
