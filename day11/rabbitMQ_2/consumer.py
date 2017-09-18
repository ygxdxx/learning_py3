#! python3

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('hello', durable=True)


def callback(ch, method, properties, body):
    print('[x] Received %s' % body.decode('utf-8'))
    # 睡眠五秒
    time.sleep(body.decode('utf-8').count('.'))
    print('[x] Done')
    # TODO 一.消息确认机制
    # 发送确认消息
    # 如果在basic_consume()中没有设置no_ack，那么这个地方就必须要设置basic_ack()方法
    # 如若不然，rabbitMQ不会释放任何没有收到反馈的消息，进而占用掉越来越多的内存空间
    # [可以通过message_unacknowledged进行debug]
    # sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
    ch.basic_ack(delivery_tag=method.delivery_tag)


# TODO Fair Dispatch
# 因为rabbitMQ发送消息是平均发送的，它并不会了解每个正在consumer正在处理的任务量是否艰巨
# 如果想让consumer等当前的task处理完成，再继续接收消息，可以通过设置以下代码完成。
channel.basic_qos(prefetch_count=1)

# TODO 一.消息确认机制
# 当生产者给消费者发送消息的时候
# 如果有多个队列同时处理接收消息，rabbitMQ会将消息平均的发送个各个接受者
# 如果在处理消息的过程当中，接受者突然死掉了，那么它当前正在处理的task就会消失，并且已经分配给queue但是还没有来得及处理的task也会消失
# 在实际情况下，rabbitMQ默认开启了消息接收确认机制，即no_ack=False。
# 其指的是，在消费者接从queue中获取了task之后会发送一条确认信息，如果生产者没有接收到这条确认信息就认为消息没有得到正确处理，会将这条消息重新放入queue中
channel.basic_consume(callback, queue='hello')

channel.start_consuming()
