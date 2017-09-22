#! python3

from day12 import orm_multi_fk
from sqlalchemy.orm import sessionmaker

Session_clz = sessionmaker(bind=orm_multi_fk.engine)
session = Session_clz()

# addr1 = orm_multi_fk.Address(street='tiantongyuan', city='shahe', state='beijing')
# addr2 = orm_multi_fk.Address(street='wudaokou', city='haidian', state='beijing')
# addr3 = orm_multi_fk.Address(street='yanjiao', city='langfang', state='hebei')
# addr_lst = [addr1, addr2, addr3]
# session.add_all(addr_lst)
#
# c1 = orm_multi_fk.Customer(name='xiaoming', bill_address=addr1, mail_address=addr2)
# c2 = orm_multi_fk.Customer(name='xiaohong', bill_address=addr3, mail_address=addr3)
# customer_lst = [c1, c2]
#
# session.add_all(customer_lst)
# session.commit()

obj = session.query(orm_multi_fk.Customer).filter(orm_multi_fk.Customer.name == 'xiaoming').first()
print(obj.name, obj.bill_address, obj.mail_address)
