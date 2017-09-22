#! python3

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='web_db', echo='True')

# 获取游标
cursor = conn.cursor()

# 返回受到影响的行数
effect_row = cursor.execute('SELECT * FROM stu')

data = [('xiaogang', 66), ('xiaohei', 55)]

# 插入一条数据
# cursor.execute('INSERT INTO stu (username,age) VALUES (\'xiaohong\',\'99\')')

# 插入多条数据
cursor.executemany('INSERT INTO stu(username,age)VALUES(%s,%s)', data)

# TODO 默认开启了事物，最后需要进行提交
conn.commit()

# 获取所有条目
print(cursor.fetchall())

# 获取前三条数据
print(cursor.fetchmany(3))

cursor.close()
