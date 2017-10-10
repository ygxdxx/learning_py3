#! python3


class Node(object):
    """数据节点ADT"""

    def __init__(self, data):
        self.elem = data
        self.prev = None
        self.next = None


class DouleLink(object):
    """双向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        pass

    def length(self):
        """返回链表长度"""
        pass

    def travel(self):
        """遍历链表中的数据"""
        pass

    def add(self, data):
        """在头部插入新的数据"""
        pass

    def append(self, data):
        """在尾部追加新的节点"""
        pass

    def insert(self, pos, data):
        """在指定位置插入节点"""
        pass

    def remove(self, data):
        """移除指定元素"""
        pass

    def search(self, data):
        """判断元素是否存在"""
        pass
