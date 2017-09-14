#! python3

import threading
import time

# 死锁
num1, num2 = 0, 0
# 递归锁
lock = threading.RLock()


def func1():
    print('grab the first part data')
    lock.acquire()
    global num1
    num1 += 1
    lock.release()
    return num1


def func2():
    print('grab the second part data')
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


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
