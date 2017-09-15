#! python3

import threading
from time import ctime, sleep


class MyThread(threading.Thread):
    def __init__(self, func, args, name=None):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name

    def get_result(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print('end', self.name, 'at:', ctime())


def fib(x):
    sleep(0.05)
    if x < 2:
        return 1
    return fib(x - 2) + fib(x - 1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return fac(x - 1) * x


def sum_x(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum_x(x - 1)


funcs = [fib, fac, sum_x]
n = 12

if __name__ == '__main__':
    nfuncs = range(len(funcs))

    print('SINGLE THREAD BEGIN**')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print('end', funcs[i].__name__, 'at', ctime())

    print('MULTIPLE THREAD BEGIN**')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        print(t.get_result())
