#! python3
__author__ = ''

import select
import socket
import queue

# TODO 使用select监测服务端程序

# 创建服务端socket实例
server = socket.socket()
server.bind(('localhost', 9998))
server.listen()

# 设置为非阻塞模式
server.setblocking(False)

# 因为最初并没有新的连接进入，自己是唯一的一个需要被监测的对象
input_sockets = [server, ]
output_sockets = []
# 发送给客户端的消息队列字典
msg_dict = {}

while True:
    # 使用select监测所有对象
    # 三个参数
    # 第一个：需要被select监测的socket
    # 第二个：返回的列表
    # 第三个：出现异常/问题的socket（与被检测的socket完全一致）
    readable_lst, writeable_lst, exceptional_lst = select.select(input_sockets, output_sockets, input_sockets)
    # 轮询读取获取的监测列表
    for r in readable_lst:
        # 如果活动的是其中存放的server对象，则代表来了一个新的连接
        if r is server:
            conn, addr = server.accept()
            print('new connection is coming...', addr)
            # 为了当客户端发送数据的时候 服务器端可以知晓 所以现在新的连接存入列表之中
            input_sockets.append(conn)
            # 初始化一个队列，存放需要返回给客户端的数据
            msg_dict.setdefault(conn)
            msg_dict[conn] = queue.Queue()
        else:
            # 因为此时为非阻塞的形式，所以不会在这里停下来 如果不加任何判断直接使用的话，客户端没有发送数据的时候肯定会报错
            data = r.recv(1024)
            print('data received:', data.decode('utf-8'))
            # 先不将接收到的数据立刻返回 通过连接对象获取对应的queue然后调用put方法将信息暂时存入其中
            msg_dict[r].put(data)
            # 存入需要返回的连接队列中
            output_sockets.append(r)

    # 循环需要返回给客户端的连接列表
    for w in writeable_lst:
        # 数据暂存列表中读取信息队列获取相应的信息
        data_to_clien = msg_dict[w].get()
        # 向客户端发送数据
        w.send(data_to_clien)
        # 已经发送过数据 现在移除本次的客户端对象
        output_sockets.remove(w)

    # 处理出现异常/错误的连接实例
    for e in exceptional_lst:
        # 1.从被监测的列表中进行删除
        input_sockets.remove(e)
        # 2.判断是否存在于返回列表中
        if e in output_sockets:
            # 从返回列表中进行移除
            output_sockets.remove(e)
        # 3.删除对应的消息队列
        del msg_dict[e]
