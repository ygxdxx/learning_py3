#! python3

import threading
import time

num1, num2 = 0, 0
lock = threading.Lock()


def func1():
    pass


def func2():
    pass


def func3():
    lock.acquire()
    res1 = func1()
    print('---between func1 and func2---')
    res2 = func2()
    lock.release()
    print(res1, res2)


for i in range(10):
    t = threading.Thread(target=func3)
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('all threads done'.center(50, '-'))
    print(num1, num2)
