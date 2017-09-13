#! python3

import threading
import time

num = 0

# 线程锁引入的原因
# 在GIL对线程进行调度的过程当中，即便给某一个线程分配了某个CPU核心进行执行
# 可能因为这个线程执行时间过长，或者执行的指令数量过多，此时这个线程就会被挂起 此时正在操作的数据会保存在CPU的寄存器中（相当保存了一个快照）
# 当下一个线程进行操作的时候，会直接从寄存机中读取此时的数据状态，而不是原本的数据
# 这可能会导致多个线程同时操作同一个数据的时候造成数据的值错乱，不符合预期
# 此时的解决办法就是引入线程锁机制，对数据操作的部分进行保护，保证同一时间只能有一个线程操作数据
# 成为了串行操作

# 先生成锁的实例
lock = threading.Lock()


def fun(name):
    # 获取锁
    # lock.acquire()
    global num
    time.sleep(0.5)
    num += 1
    # 释放锁
    # lock.release()


thread_objs = []
for i in range(100):
    t = threading.Thread(target=fun, args=('%s' % i,))
    t.start()
    thread_objs.append(t)

for i in range(len(thread_objs)):
    # 如果不适用join 不会等待子线程执行完毕，主线程和子线程并行
    # 直接执行到41行代码
    thread_objs[i].join()

print('total num:', num)
