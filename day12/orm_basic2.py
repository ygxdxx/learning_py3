#! python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 1.创建引擎
engine = create_engine('mysql+pymysql://root:123@localhost:3306/web_db', encoding='utf-8', echo=True)

# 2.生成基类
Base = declarative_base()


# 3.创建表结构类 继承基类
class Student(Base):
    # 表名
    __tablename__ = 'student'
    # 字段
    id = Column(Integer, primary_key=True)
    name = Column(String(8), nullable=False)
    gender = Column(String(8))
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return 'id:%s name:%s gender:%s score:%s' % (self.id, self.name, self.gender, self.score)


# 4.执行创建表结构操作，将引擎当作参数进行传入
Base.metadata.create_all(engine)

# 5.添加数据 创建sessionmaker
Session_clz = sessionmaker(bind=engine)
# 创建session对象
session = Session_clz()

# 6.创建Base基类的子类对象，并传入数据
stu_obj_1 = Student(id=1, name='xiaoming', gender='male', score=79)
stu_obj_2 = Student(id=2, name='xiaogang', gender='male', score=87)
stu_obj_3 = Student(id=3, name='xiaohong', gender='female', score=99)
lst_objs = [stu_obj_1, stu_obj_2, stu_obj_3]

# 7.将创建好的对象传入到session中
session.add_all(lst_objs)

# 8.提交事物
session.commit()
