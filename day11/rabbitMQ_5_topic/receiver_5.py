#! python3

import pika


def callback(ch, method, properties, body):
    print('RECEIVED %s' % body.decode('utf-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
queue_res = channel.queue_declare(durable=True, exclusive=True)
queue_name = queue_res.method.queue
channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')
channel.queue_bind(exchange='topic_exchange', queue=queue_name, routing_key='a.b.c.d.e')
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
