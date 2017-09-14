#! python3

import threading
import time


# TODO Python中的Event
# 处理机制过程：
#   全局定义了一个Flag，初始为False。
#   如果Flag为Flase，则 wait() 的线程就会进入阻塞状态
#   如果Flag为True，则 wait() 的线程便不再阻塞

# TODO 对象方法
# Event事件用于主线程控制其他线程的执行，事件主要提供了三个方法
#   1. wait() 进入等待状态
#   2. clear() 将设为False
#   3. set() 将Flag设置为True
# threading.Event可以使一个线程等待其他线程的通知，把这个Event传递到线程对象中
# 一旦该线程通过wait()方法进入等待状态，直到另一个线程调用该Event的 set() 方法将内置标志设置为True时，该Event会通知所有等待的线程恢复运行

def func(t_name, signal_e):
    print('I am %s,I will sleep...' % t_name)
    # 进入等待状态
    signal_e.wait()
    print('I am %s,I awake...' % t_name)


if __name__ == '__main__':
    # 获取event
    signal = threading.Event()
    thread_objs = []
    for i in range(3):
        t = threading.Thread(target=func, args=('thread_%s' % i, signal))
        thread_objs.append(t)
    for t in thread_objs:
        t.start()

    print('main thread sleep 3 seconds...')
    time.sleep(2)

    inp = input('continue sleep? y/n:\n')
    if inp == 'y':
        # 唤醒所有阻塞线程
        signal.set()
    elif inp == 'n':
        # 让所有线程继续阻塞
        signal.clear()
        print('sleep 2 seconds more...')
        time.sleep(2)
        print('awake all threads')
        signal.set()
