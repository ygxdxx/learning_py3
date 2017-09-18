#! python3

import pika

# TODO 广播
# 之前的案例中，
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 避免重复建立TCP连接
channel = connection.channel()
# 因为是广播模式，所以创建的queue不需要指定名字，让rabbit起一个随机名称
# exclusive=True保证如果这个queue断开了连接这个queue就会被删除
channel.queue_declare(durable=True, exclusive=True)

# 此处exchange不再为空，需要为其添加名字
# 参数type = 'fanout' 表明这个exchange会将收到的消息发送给其所知的所有queue
# 补充：
# 可以使用命令 sudo rabiitmqctl list_exchanges 列出当前所有的exchange
# 其中会包含一个名为 amq.* 的exchange，这是由rabbitmq默认创建的exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 一直没有显式的创建exchange也能照常发送消息原因就在于我们使用了rabbitmq默认的exchange，exchange=''
# routing_key 用于设置exchange需要将消息发送到哪个queue中，现在处于广播模式所以就不需要设定routing_key的值了
channel.basic_publish(exchange='logs', routing_key='', body='This is a broascast message')

connection.close()
