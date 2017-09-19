#! python3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')
queue_res = channel.queue_declare(durable=True, exclusive=True)
queue_name = queue_res.method.queue
# 需要接收发送过来的消息的队列需要在进行绑定的时候再queue_bind()中添加一个 routing_key=？的参数
channel.queue_bind(exchange='direct_exchange', queue=queue_name, routing_key='info')


def callback(ch, method, properties, body):
    print('[x] received message %s' % body.decode('utf-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
