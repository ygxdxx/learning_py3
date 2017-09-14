#! python3

from multiprocessing import Lock, Process
import time


# TODO 进程锁
# 如果不加进程锁，打印的时候顺序可能会错乱
# 使用线程锁来解决问题

def func(l, index):
    # 获取锁
    l.acquire()
    time.sleep(1)
    print('hello', index)
    # 释放锁
    l.release()


if __name__ == '__main__':
    # 创建锁对象
    lock = Lock()

    # 启动10个进程
    for i in range(10):
        # 将锁对象传递给进程
        Process(target=func, args=(lock, i)).start()
