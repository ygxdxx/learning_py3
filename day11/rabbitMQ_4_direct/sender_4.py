#! python3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(durable=True, exclusive=True)
# TODO 广播过滤
# fanout的广播模式意味着所有的订阅者都会接收到请求，如果想让信息产生的过滤的效果就需要
# 将exchange的模式由fanout修改为direct
channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')
channel.basic_publish(exchange='direct_exchange', routing_key='info', body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2))
print('[x] Sended...')
connection.close()
