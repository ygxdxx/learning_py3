#! python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://root:123@localhost:3306/fk_test')

Base_clz = declarative_base()


class Book(Base_clz):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author', secondary='book_2_author', backref='books')

    def __repr__(self):
        return self.name


class Author(Base_clz):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


class Book2author(Base_clz):
    """
    关联表
    """
    __tablename__ = 'book_2_author'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), primary_key=True)

    def __repr__(self):
        pass


Base_clz.metadata.create_all(engine)
