import datetime

from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from db_engine.model import City, Country, State, Category, MarketCategory, User, Review
from resources.cvsdb_read import (get_states, get_categories, get_countries,
                                  get_cities, write_city_id, get_markets)


def seed_all_data(engine):
    Session = sessionmaker(engine)

    states = get_states()
    #добавляем штаты - done
    with Session() as session:
        try:
            i = 0
            for state in states:
                session.add(State(name=state))
                i += 1
            session.commit()
            print(f"Added states rows: {i}")
        except Exception as e:
            raise e
    del states

    # берем штаты с ID
    with Session() as session:
        try:
            states = session.query(State).all()
        except Exception as e:
            raise e

    #читаем округа из файла и готовим для записи в БД
    countries = get_countries(states)

    #добавляем округа в БД
    with Session() as session:
        try:
            i = 0
            for country in countries:
                session.add(Country(name=country[0], state_id=country[1]))
                i += 1
            session.commit()
            print(f"Added countries rows: {i}")
        except Exception as e:
            raise e
    del countries

    with Session() as session:
        try:
            countries = session.query(Country).all()
        except Exception as e:
            raise e

    #читаем города из файла и готовим для записи в БД
    cities = get_cities(countries)
    # for city in cities:
    #     print(city)

    #добавляем города в БД
    with Session() as session:
        try:
            i = 0
            for city in cities:
                session.add(City(name=city[0], country_id=city[1]))
                i += 1
            session.commit()
            print(f"Added cities rows: {i}")
        except Exception as e:
            raise e

    del cities

    # берем из БД города с ID и записываем ID в ExportCityID.csv
    with Session() as session:
        try:
            cities = session.query(City).all()
            write_city_id(cities)
        except Exception as e:
            raise e

    #берем категории из ExportCityID.csv для записи в БД
    categories = get_categories()
    # запись категорий в БД
    with Session() as session:
        try:
            session.add_all(categories)
            session.commit()
            print("Added categories")
        except Exception as e:
            raise e
    del categories

    # берем из БД категории с ID
    with Session() as session:
        try:
            categories = session.query(Category).all()
        except Exception as e:
            raise e

    #записываем рынки в БД
    markets, mark_cat = get_markets(categories)
    with Session() as session:
        try:
            session.add_all(markets)
            for item in mark_cat:
                mark_id, cat_id = item
                session.add(MarketCategory(market_id=mark_id, category_id=cat_id))
            session.commit()
            print("Added markets, markets-categories")
        except Exception as e:
            raise e

    with Session() as session:
        try:
            session.add_all(
                [
                    User(
                        fname="Геннадий",
                        lname="Гаврилов",
                        username="ben",
                        passhash=r"e4432baa90819aaef51d2a7f8e148bf7e679610f3173752fabb4dcb2d0f418d3"),
                    User(
                        fname="Акакий",
                        lname="Фермеров",
                        username="set",
                        passhash=r"1402946ccbc2a03323f5f40548684a2428789ad5507a6ca12d5bb671cb78c315")
                ]
            )
            session.commit()

            session.add_all(
                [
                    Review(
                        user_id=1,
                        market_id=1000021,
                        score=5,
                        review="Good market, nice goods",
                        datetime=datetime.datetime(2024,6,18,3,12,30)),
                    Review(
                        user_id=2,
                        market_id=1000021,
                        score=4,
                        review="It's ok",
                        datetime=datetime.datetime(2024,6,20,21))
                ]
            )
            session.commit()
            print("Added markets, markets-categories")
        except Exception as e:
            raise e


def create_db_user(engine):
    user_create = text(r"""CREATE ROLE marketuser WITH 
    LOGIN
    NOSUPERUSER
    INHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION
    ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:OY9y6ZCZhDYd8AG0zWeqBg==$+I1MJ7ESzyMfalEJEoHQYe55z+BHlweU1Fp+Thg4d1c=\:O7S90XAXsZdFePwfnR3Gqo3K+AGVNgcLIZpDW/t6Pq4=';""")

    alter_user = ["GRANT CONNECT ON DATABASE farmersmarkets TO marketuser;",
                  "GRANT ALL ON SCHEMA public TO marketuser;",
                  "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO marketuser;",
                  "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO marketuser;"]

    connection = engine.connect()
    trans = connection.begin()
    try:

        connection.execute(user_create)
        for statement in alter_user:
            connection.execute(text(statement))
        trans.commit()
    except Exception:
        trans.rollback()
        raise
