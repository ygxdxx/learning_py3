#! python3

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# echo=True
engine = create_engine('mysql+pymysql://root:123@localhost:3306/web_db', encoding='utf-8')

# 生成基类
Base = declarative_base()


# 需要创建表结构的类
class User(Base):
    # 表名
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<id:%s name:%s>' % (self.id, self.name)


# 将所有继承了基类的类都进行执行
# TODO 此处创建了表结构
Base.metadata.create_all(engine)

# TODO 插入数据
# 首先创建与数据库会话的session类，参数中需要绑定engine引擎 相当于cursor
Session_clz = sessionmaker(bind=engine)
# 创建session类相应的实例
session = Session_clz()

# 生成需要创建数据对象 代表着添加了一条记录
"""
user_obj1 = User(name='xiaoming', password='123456')
user_obj2 = User(name='xiaohong', password='123')
"""
# 将添加好数据的对象传入到session对象的add方法中
"""
session.add(user_obj1)
session.add(user_obj2)
"""
# 提交数据代表将数据上述所有记录添加到表中
"""
session.commit()
"""

# TODO 查询
# all()获取到的是一个列表对象，可能有多个
# first()可以获取表中符合条件的第一个对象
# 多条件查询就使用多个filter方法进行组合
# data = session.query(User).filter_by(name='xiaoming').all()
data = session.query(User).filter(User.id > 2).filter(User.id < 3).all()
# print(data[0])

# TODO 修改
# 直接对属性赋值即可
# data[0].name = 'xiaobai'
# session.commit()

# TODO 统计和分组
# 1.统计使用count()函数
# 2.分组使用group_by()函数
# 可以在filter()函数中使用like()函数进行模糊匹配
print(session.query(User).filter(User.id > 2).count())
