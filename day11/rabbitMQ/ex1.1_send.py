#! python3

import pika

# 1.建立连接
# 因为是在本机上进行试验，所以使用localhost即可
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 2.发送消息之前，必须要确认接收方的queque处于一个存在状态，否则MQ会丢弃这条信息
channel = connection.channel()

# 3.发送hello
# 确保接收方的queue必须存在，所以创建一个queue用于将消息发送到其中
channel.queue_declare(queue='hello')

# 4.queue的名字必须通过routing_key参数进行制定
# 通过channel发送的数据并不会直接到达之前的queue中，而是**必须**先通过rabbitMQ的数据交换环节，即exchange
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print('[x] Sent Hello World!')

# 5.我们必须要去人缓冲区已经flushes，我们发送回的消息才真的得到的发送，close可以完成这个目的
connection.close()
