#! python3

# 1.push(elem) 压入元素
# 2.pop() 弹出栈顶元素
# 3.peek() 获取栈顶元素 但不删除


class Stack(object):
    """栈"""

    def __init__(self):
        """创建一个新的栈"""
        self.__list = []

    def push(self, elem):
        """将一个新的元素压到栈顶"""
        self.__list.append(elem)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        return self.__list[-1]

    def is_empty(self):
        """判断栈是否为空"""
        # return self.__list == []
        if len(self.__list) == 0:
            return True
        else:
            return False

    def size(self):
        """返回元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
