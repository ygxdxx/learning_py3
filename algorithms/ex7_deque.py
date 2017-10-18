#! python3

# 1. Deque() 创建一个双端队列
# 2. add_front(elem) 在对头加入一个元素
# 3. add_tail(elem) 在对尾加入一个元素
# 4. remove_front() 从对头删除一个元素
# 5. remove_tail() 从对尾删除一个元素
# 6. is_empty() 判空
# 7. size() 返回队列长度


class Deque(object):
    def __init__(self):
        """创建双端队列"""
        self.__deque = []

    def add_front(self, elem):
        """在头部添加元素"""
        self.__deque.insert(0, elem)

    def pop_front(self):
        """移除头部元素"""
        if self.is_empty():
            return None
        return self.__deque.pop(0)

    def add_tail(self, elem):
        """在尾部添加元素"""
        self.__deque.append(elem)

    def pop_tail(self):
        """移除尾部元素"""
        if self.is_empty():
            return None
        return self.__deque.pop(-1)

    def is_empty(self):
        """判断是否为空"""
        return self.__deque == []

    def size(self):
        """返回队列长度"""
        return len(self.__deque)


if __name__ == '__main__':
    dq = Deque()