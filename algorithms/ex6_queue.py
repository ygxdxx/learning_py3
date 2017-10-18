#! python3

# 1. Queue() 创建一个队列
# 2. enqueue(elem) 入队
# 3. dequeue() 出队
# 4. size() 长度
# 5. is_empty() 判空


class Queue(object):
    def __init__(self):
        """初始化队列"""
        self.__queue = []

    def enqueue(self, elem):
        """入队"""
        self.__queue.append(elem)

    def dequeue(self):
        """出队"""
        if self.is_empty():
            return None
        return self.__queue.pop(0)

    def size(self):
        """队列长度"""
        return len(self.__queue)

    def is_empty(self):
        """判空"""
        return self.__queue == []


if __name__ == '__main__':
    q = Queue()
