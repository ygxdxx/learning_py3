#! python3

from multiprocessing import Manager, Process


# TODO Manager
# 无论是 queque 还是 pipe 都只是在多个进程进行数据的传递
# 现在可以通过manager达到多进程之间数据的共享，而非单纯的传递

def func(d, l):
    d[1] = 'one'
    d[2] = 'two'
    d[3] = 'three'

    l.append('小明')
    l.append('小红')
    l.append('小刚')


if __name__ == '__main__':
    with Manager() as manager:
        # 生成一个可共享的字典
        dic = manager.dict()
        # 生成一个可共享的列表
        lst = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=func, args=(dic, lst))
            p.start()
            p_list.append(p)
        for item in p_list:
            item.join()
        print(dic)
        print(lst)
