#! python3

import multiprocessing
import os


def func(name):
    print('process name:', name)
    print('moudle name:', __name__)
    # 获取父进程id
    print('parent process id:', os.getppid())
    # 获取当前进程id  - pycharm
    print('current process id:', os.getpid())


def func_process(name):
    print('process name:', name)
    print('parent process id:', os.getppid())
    print('current process id:', os.getpid())


if __name__ == '__main__':
    func('main_process')
    p = multiprocessing.Process(target=func_process, args=('child_process',))
    print('\n')
    p.start()
    p.join()
