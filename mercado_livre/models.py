from sqlalchemy import Column, ARRAY, Boolean, String, create_engine, DateTime
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base


from decouple import config
import datetime


DATABASE_URL = config("DATABASE_URL").replace("postgres://", "postgresql://", 1)
DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(DATABASE_URL)


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    """
    Defines the items model
    """

    __tablename__ = "mercado_livre_offers"

    product_name = Column("name", String, primary_key=True)
    product_categories = Column("categories", ARRAY(String))
    best_seller = Column("best_seller", ARRAY(String))
    offer_of_the_day = Column(" offer_of_the_day", Boolean)
    product_discount = Column("discount", String)
    product_old_price = Column("old_price", String)
    product_new_price = Column("new_price", String)
    date = Column(
        DateTime(timezone=False), default=datetime.datetime.now().strftime("%m/%d/%Y")
    )
