#! python3

import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        queue_res = self.channel.queue_declare(exclusive=True)
        self.callback_queue = queue_res.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.channel.basic_publish(exchange='', routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id, ), body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()
print('[X] Requesting fib(10)')
response = fibonacci_rpc.call(10)
print('[X] Result is %s' % str(response))
