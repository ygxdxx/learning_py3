#! python3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('hello', durable=True)

while True:
    # TODO 二.队列和消息持久化
    # 可以通过消息确认机制解决客户端崩溃数据丢失的问题，但是如果服务器崩溃了只能把队列和消息进行保存解决
    # 1.保证queue持久化保存：在声明队列即queue_declare()的时候添加参数 durable=Ture 即可完成（rabbitMQ不允许对已经存在的queue修改参数，所以换一个queue名称进行测试）
    # 2.保证message消息持久化：只是把queue持久化还是不够的，因为队列中的消息会被清空。需要在basic_publish()的时候添加参数delivery_mode=2来完成消息持久化
    # 但是，即便通过这两个参数设定了队列和消息持久化，也不能完全的保证不出现问题。因为，把数据从内容中保存到硬盘这段时间还是可能出现问题
    message = input('>> input your message:\n')
    channel.basic_publish(exchange='', routing_key='hello', body=message,
                          properties=pika.BasicProperties(delivery_mode=2))
    print('[x] Sent %s to Receiver' % message)

# connection.close()
