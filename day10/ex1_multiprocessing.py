#! python3

import multiprocessing
import threading
import time


# TODO 多进程 multiprocessing
# 从2.6开始引入，允许为多核或多CPU派生进程，其接口与threading模块十分相似
# 其中也包含了在共享任务进程间传输数据的多种方式

def func2_run(name):
    time.sleep(1)
    print('hello thread %s' % name)


def func_run(name):
    time.sleep(1)
    print('hello process %s' % name)
    # 在一个进程当中开启一个新的线程
    t = threading.Thread(target=func2_run, args=('线程',))
    t.start()
    t.join()


# 创建一个新的进程
p = multiprocessing.Process(target=func_run, args=('进程',))
p.start()
