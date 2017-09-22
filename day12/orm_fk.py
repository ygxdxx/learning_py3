#! python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# 1.创建引擎
engine = create_engine('mysql+pymysql://root:123@localhost:3306/fk_test', encoding='utf-8')

# 2.生成基类
Base = declarative_base()


# 3.创建表结构类 继承基类
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return 'id:%s name: %s' % (self.id, self.name)


class StuRecord(Base):
    __tablename__ = 'stu_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))

    # 让学生表和记录表建立双向关联
    # 可以通过通过record中的student字段查询学生表内容
    # 反过来，可以通过学生表中的record字段查询记录表的内容
    student = relationship('Student', backref='record')

    # 或者 在当前类中建立另外一个对象的引用
    # student = Student()
    def __repr__(self):
        return 'day:%s status:%s' % (self.day, self.status)


# 4.执行创建表结构操作，将引擎当作参数进行传入
Base.metadata.create_all(engine)

# 5.添加数据 创建sessionmaker
Session_clz = sessionmaker(bind=engine)
# 创建session对象
session = Session_clz()

"""
# 6.创建Base基类的子类对象，并传入数据
s1 = Student(name='xiaoming1', register_date='2017-09-21')
s2 = Student(name='xiaoming2', register_date='2017-09-22')
s3 = Student(name='xiaoming3', register_date='2017-09-23')
s4 = Student(name='xiaoming4', register_date='2017-09-24')
stu_lst = [s1, s2, s3, s4]

r1 = StuRecord(day=1, status='YES', stu_id='1')
r2 = StuRecord(day=2, status='YES', stu_id='1')
r3 = StuRecord(day=3, status='NO', stu_id='1')
r4 = StuRecord(day=1, status='YES', stu_id='2')
record_lst = [r1, r2, r3, r4]

# 7.将创建好的对象传入到session中
# session.add_all(stu_lst)
session.add_all(record_lst)

# 8.提交事物
session.commit()
"""

# 9.查询
# stu_obj = session.query(StuRecord).filter(StuRecord.stu_id == 1).all()
# print(stu_obj)

stu_obj = session.query(Student).filter(Student.name == 'xiaoming1').first()
# 返回的是record表中的记录，即repr返回的表数据格式
print(stu_obj.record)
