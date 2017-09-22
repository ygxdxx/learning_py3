#! python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:123@localhost:3306/fk_test')

Base_clz = declarative_base()


class Address(Base_clz):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return 'state:%s city:%s street:%s' % (self.state, self.city, self.street)


class Customer(Base_clz):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    bill_address_id = Column(Integer, ForeignKey('address.id'))
    mail_address_id = Column(Integer, ForeignKey('address.id'))

    # 连接多个外键的时候，反向查询的时候无法区分到底是哪个字段 所以需要加一个属性foreign_keys=[]
    bill_address = relationship('Address', foreign_keys=[bill_address_id])
    mail_address = relationship('Address', foreign_keys=[mail_address_id])

    def __repr__(self):
        return 'id:%s name:%s bill_address:%S mail_address:%s' % (
            self.id, self.name, self.bill_address, self.mail_address)


Base_clz.metadata.create_all(engine)
