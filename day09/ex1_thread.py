#! python3

import threading
import time


def run(n):
    for i in range(100):
        time.sleep(0.1)
        print(n, ' : ', i)


# 创建两个线程对象
t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))

# 此处会等待两秒钟
# t1执行完以后t2才会继续执行
"""
t1.run()
t2.run()
"""

# 开启线程
"""
t1.start()
"""

# join() 等待当前线程执行完毕后才继续向下执行
"""
t1.join()
"""

# current_thread() 返回当前正在执行的线程
"""
print(threading.current_thread())
"""

# active_acount() 返回当前正在执行的线程数量


# TODO 守护线程
# 指在程序运行的时候在后台提供一种通用服务的线程，比如垃圾回收线程就是一个很称职的守护者，并且这种线程并不属于程序中不可或缺的部分。
# 因此，当所有的非守护线程结束时，程序也就终止了，同时会杀死进程中的所有守护线程。
# 反过来说，只要任何非守护线程还在运行，程序就不会终止。
"""
t1.setDaemon(t1)
"""

# TODO 全局解释器锁GIL
# 在CPython中，即便是多核心的CPU，有多个线程同时存在，在同一时间只会有一个线程被解释器执行。
# 这样可以避免多个线程同时操作一个数据会造成
# 这个操作完全是由全局解释器锁GIL来控制的，步骤如下：
# 1.设置GIL
# 2.切换一个线程去运行
# 3.执行下面操作之一
#   (1) 指定数量的字节码指令
#   (2) 线程主动让出控制权 （由CPU制定的执行时间和指令数量决定）
# 4.把线程设置回睡眠状态（切换出线程）
# 5.解锁GIL
# 6.再次重复以上步骤
