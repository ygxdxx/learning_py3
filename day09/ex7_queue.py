#! python3

import queue

# TODO 1.Python中的queue
# Queue是Python标准库中线程安全的队列(FIFO)实现，提供了一个适用于多线程编程的先进先出的数据结构，用于在生产者和消费者之间进行信息传递
# 可以实现线程的有序保存和回调，看似list也可以实现同样的功能。但是list中保存的是对象内存地址的应用，取出以后仍然会停留在list之中
# (queue类似于Java中的threadlocal)？

# TODO 2.分类
# 1.Queue(maxsize=?) FIFO队列，如果给定了最大值没有空间时会阻塞，如果没有指定则为无限队列。
# 2.LifoQueue(maxsize=?) LIFO队列，如果给定了最大值没有空间时会阻塞，如果没有指定为无限队列
# 3.PriorityQueue(maxsize=?) 优先级队列，如果给定了最大值没有空间时会阻塞，如果没有指定为无限队列

# TODO 3.异常
# 1. Empty 对空队列调用get()方法的时候抛出异常
# 2. Full 对已满的队列调用put()方法的时候抛出异常

# TODO 4.对象方法
# 1.qsize() 返回当前队列的大小，可能随时被线程修改，会返回近似值
# 2.empty() 如果队列为空返回True，不为空返回False
# 3.full() 如果队列满了返回True，没有满返回False
# 4.put(item,block=True,timeout=None) 如果block为True，设置阻塞时等待的时间到了后会抛出异常
# 5.get(block=True,timeout=None) 如果block为True，则一直阻塞到有可用的元素为止
# 6.task_done() 表示队列中的上一个任务已经执行完成，该方法会被下面的join调用
# 7.join() 队列中所有的元素执行完毕并调用上面的task_done()信号之前，保持阻塞状态

# TODO queue中join()和task_done()关系

# 1.
q1 = queue.Queue(maxsize=5)
# 存入元素
q1.put('小明', block=True, timeout=3)
q1.put('小红')
q1.put('小刚')
# 获取元素
print(q1.get())
# 打印当前队列的长度
print(q1.qsize())
while not q1.empty():
    print(q1.get())


print('seprator'.center(30, '-'))

# 2.
q2 = queue.LifoQueue()
q2.put('小明')
q2.put('小红')
q2.put('小刚')
# 先取出最后一个
print(q2.get(block=True, timeout=3))

print('seprator'.center(30, '-'))

# 3.
q3 = queue.PriorityQueue()
# 传入元组
q3.put((3, '小明'))
q3.put((1, '小红'))
q3.put((5, '小刚'))
for i in range(q3.qsize()):
    print(q3.get())
