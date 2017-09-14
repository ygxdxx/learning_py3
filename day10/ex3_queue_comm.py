#! python3

import threading
import queue
from multiprocessing import Process, Queue


# TODO 进程间的通信
# 通过queue在主线程和子线程之间可以传递数据，从而实现通信；但是在多个进程之间则无法实现


def thread_func():
    q.put('你好 子线程')


def process_func(q):
    q.put('你好 子进程')


if __name__ == '__main__':
    # 这是一个线程queue队列
    q = queue.Queue()
    # 这是一个进程queue队列
    q_2 = Queue()
    """
    t = threading.Thread(target=thread_func)
    t.start()
    print(t_q.get())
    """
    # 将创建好的进程queue对象当作参数传入给子进程以后，看上去是单一对象的传递
    # 但是实际上已经不是同一个queue了，只是数据从两个进程之间互相传递
    # 首先把外部创建好的queue中的数据进行pickle的序列化存放到第三方的位置，子进程获取到这个queue之后把之前序列化好的数据再次进行pickle的反序列化
    p = Process(target=process_func, args=(q_2,))
    p.start()
    print(q_2.get())
