#! python3

from day12 import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_clz = sessionmaker(bind=orm_m2m.engine)
session = Session_clz()

b1 = orm_m2m.Book(name='Java', pub_date='2017-09-21')
b2 = orm_m2m.Book(name='Python', pub_date='2017-09-22')
b3 = orm_m2m.Book(name='Go', pub_date='2017-09-23')
book_lst = [b1, b2, b3]

a1 = orm_m2m.Author(name='xiaoming')
a2 = orm_m2m.Author(name='xiaohong')
a3 = orm_m2m.Author(name='xiaogang')
author_lst = [a1, a2, a3]

# 让两个表的多个数据之间建立关联
# b1.authors = [a1, a2]
# b2.authors = [a1]
# b3.authors = [a2, a3]
#
# session.add_all(book_lst)
# session.add_all(author_lst)

# TODO 查询
# 查询xiaoming创作的所有图书
author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == 'xiaoming').first()
print(author_obj.books)
print(author_obj.books[0].pub_date)

# 查询名称为Java的书的所有作者
book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.name == 'Java').first()
print(book_obj.authors)

# TODO 删除
# 直接删除即可 不需要维护第三张表
# 需要把对应记录的对象传入进去
# book_obj.authors.remove(author_obj)

# 提交
# session.commit()
