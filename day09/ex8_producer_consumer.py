#! python3

import threading
import time
import queue

q = queue.Queue()


def producer(p_name):
    count = 1
    while True:
        time.sleep(0.3)
        print('%s 存入第 %s 颗巧克力...' % (p_name, count))
        q.put('巧克力_%s' % count)
        count += 1


def consumer(c_name):
    # while not q.empty():
    while True:
        time.sleep(0.1)
        print('%s 取到了 %s 并吃掉了它...' % (c_name, q.get()))
    else:
        print('这里没有吃的了')


# 创建两个线程对象
p_thread = threading.Thread(target=producer, args=('生产者',))
c_thread = threading.Thread(target=consumer, args=('消费者',))

# 开启两个线程
c_thread.start()
p_thread.start()
