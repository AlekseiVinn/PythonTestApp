from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, REAL, Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
metadata = Base.metadata


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey("countries.id"))
    markets = relationship("Market", backref="cities")

    def __repr__(self):
        return self.name


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cities = relationship("City", backref="countries")
    state_id = Column(Integer, ForeignKey("states.id"))


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    countries = relationship("Country", backref="states")
    name = Column(String)

    def __repr__(self):
        return self.name


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('users.id'))
    market_id = Column("market_id", Integer, ForeignKey('markets.id'))
    datetime = Column(DateTime)
    #todo - добавить ограничение score
    score = Column(Integer)
    review = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    reviews = relationship("Market", secondary="reviews", back_populates="reviews", lazy=False)

    fname = Column(String)
    lname = Column(String)
    username = Column(String)
    passhash = Column(String)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    markets = relationship("Market", secondary="markets_categories", back_populates="categories")
    name = Column(String)

    def __repr__(self):
        return f"Category: id {self.id}, {self.name}"


class Market(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True, autoincrement=False )
    city_id = Column(Integer, ForeignKey("cities.id"))
    reviews = relationship("User", secondary="reviews", back_populates="reviews", lazy=False)
    categories = relationship("Category", secondary="markets_categories", back_populates="markets", lazy=False)

    name = Column(String)

    website = Column(String)
    facebook = Column(String)
    twitter = Column(String)
    youtube = Column(String)
    media = Column(String)

    season1date = Column(String)
    season1time = Column(String)
    season2date = Column(String)
    season2time = Column(String)
    season3date = Column(String)
    season3time = Column(String)
    season4date = Column(String)
    season4time = Column(String)

    street = Column(String)
    zip = Column(String)
    lat = Column(REAL)
    lon = Column(REAL)
    loc = Column(String)

    credit = Column(Boolean)
    wic = Column(Boolean)
    wiccsah = Column(Boolean)
    sfmnp = Column(Boolean)
    snap = Column(Boolean)

    lastupdated = Column(String)


class MarketCategory(Base):
    __tablename__ = "markets_categories"

    id = Column(Integer, primary_key=True)
    market_id = Column("market_id", Integer, ForeignKey("markets.id"))
    category_id = Column("category_id", Integer, ForeignKey("categories.id"))
