#! python3

import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql://root:123@localhost:3306/web_db', encoding='utf-8', echo='True')

Base = declarative_base()


class User(Base):
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)
