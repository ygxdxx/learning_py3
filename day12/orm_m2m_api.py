#! python3

from day12 import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_clz = sessionmaker(bind=orm_m2m.engine)
session = Session_clz()

