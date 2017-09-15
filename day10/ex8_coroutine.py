#! python3

# TODO 协程
# 协程也成为微线程，纤程。就是一种用户态的轻量级线程。
# 协程拥有自己的寄存器上下文和栈，协程调度切换时，将寄存器上下文和栈保存到其他地方。再切换回来的时候，会恢复之前保存的寄存器上下文和栈。
# 因此可以保留上一次调用时的状态，相当于保存了一个快照。

# TODO 1.协程的好处：
# 1. 无需上下文切换开销
# 2. 无需原子操作锁定同步开销
# 3. 方便切换控制流，简化编程模型
# 4. 高并发+高拓展性+低成本
# TODO 2.协程的缺点：
# 无法使用多核资源，因为其本质并不是线程。还是单线程模型，因此需要和多进程配合才能运行在多核CPU之上。


def consumer(name):
    print('starting eat food...')
    while True:
        # TODO 一个func添加了yield之后就成为了一个生成器generator() 这时候才可以调用__next()__方法
        new_food = yield
        print('[%s] is eating food %s' % (name, new_food))


def producer():
    # 只是让consumer变成生成器generator
    c1.__next__()
    c2.__next__()
    count = 0
    while True:
        count += 1
        # TODO send一共有两个作用 1. 重启生成器 2. 将数据发送给生成器
        c1.send('包子')
        c2.send('馒头')


if __name__ == '__main__':
    # 直接执行consumer()并不会执行方法中的内容
    c1 = consumer('小明')
    c2 = consumer('小红')
    # producer()
