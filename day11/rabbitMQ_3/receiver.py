#! python3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 因为是广播模式 所以不需要填写queue的名字 会随机起名
# durable 队列持久化
# exclusive 如果结束后就会将queue从内从中移除
queue_res = channel.queue_declare(durable=True, exclusive=True)

# 与发送一致
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 将queue和channel进行绑定
queue_name = queue_res.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)


# 回调函数
def callback(ch, method, properties, body):
    print('[x] %s' % body.decode('utf-8'))
    # 消息通知确认
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
