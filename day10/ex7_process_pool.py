#! python3

import time
import os
from multiprocessing import Pool


# TODO 进程池
# 降低进程启动销毁的时间，提高进程的利用率
#   pool = Pool(processes=?)
#   pool.apply(func=?,args=(?,),callback=?)
#   pool.apply_async(func=?,args=(),callback=?)
#   pool.close()
#   pool.join()

def foo(n):
    time.sleep(2)
    print('in process', os.getpid())
    return n + 100


def bar(arg):
    print('exec done', arg, os.getpid())


if __name__ == '__main__':
    print('main_pid', os.getpid())
    # 允许同时将5个进程放入进程池
    pool = Pool(processes=5)
    for i in range(5):
        # 1.串行执行
        # pool.apply(func=foo, args=(i,),callback=bar)
        # 2.异步执行
        pool.apply_async(func=foo, args=(i,), callback=bar)
    # TODO close()方法一定要在join()前面
    pool.close()
    # 等待线程池的执行结果才会结束
    pool.join()
    print('end')
