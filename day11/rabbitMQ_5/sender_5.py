#! python3

import pika

# TODO topic模式过滤
# 除了可以过滤需要接收的消息之外，我们还可以进行更细致的过滤
# 首先在声明exchange的时候将type声明为topic
# 此时在routing_key=？中就不能是单一的了，这里的值可以是一个列表，中间使用.进行分割，上限是255个字节
# 在进行bind的时候，routing_key的值也应该和之前创建的时候保持一致
# *可以在列表中代替一个词，#可以代替0或多个词

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')
channel.basic_publish(exchange='topic_exchange', routing_key='a.b.c', body='Hello this is a topic message')
print('SENT!')
connection.close()
