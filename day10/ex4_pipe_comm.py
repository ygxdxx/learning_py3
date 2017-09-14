#! python3

from multiprocessing import Process, Pipe


# TODO 通过pipe管道实现多进程间的通信
# 与socket的通信十分相似

def func(conn):
    conn.send('hello parent process [from child]')
    res_parent = conn.recv()
    # 打印来自父进程的数据
    print(res_parent, '[from parent]')


if __name__ == '__main__':
    # 同时获取父子两个接口
    conn_child, conn_parent = Pipe()
    # 将获取的pipe子对象传递给子进程
    p_child = Process(target=func, args=(conn_child,))
    p_child.start()
    # 1.通过pipe父对象接收子对象发送的数据
    res = conn_parent.recv()
    print(res)

    # 2.通过pipe父对象向子进程发送数据
    conn_parent.send('hello child process')
