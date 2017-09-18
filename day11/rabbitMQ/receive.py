#! python3

import pika

# 这部分代码都是相同的
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 1.首先要确认的事情就是消息queue队列的存在
# 之所以要重复执行这个步骤的原因就是，无法保证是哪一方先得到执行。
# 如果发送方的先开启，则queue会创建没有任何问题；如果接收方先执行则没有queue创建，消息接收会失败
# (可以通过命令：rabbitmqctl list_queues 查看当前所有的队列)
channel.queue_declare(queue='hello')


#  接收端的代码会稍微复杂一些
#  2.注册一个回调函数，当有新的消息进来的时候回调函数会得到执行
def callback(ch, method, properties, body):
    print('Received data %s' % body.decode('utf-8'))


# 3. 注册回调函数，并从消息队列queue中收取消息，一定要确保queue队列已经存在queue_declare()
channel.basic_consume(callback, queue='hello', no_ack=True)

# 4. 让接收端处于循环状态。当有消息进来，直接调用回调函数
channel.start_consuming()
