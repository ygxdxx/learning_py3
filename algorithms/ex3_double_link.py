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
        return self.__head is None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表中的数据"""
        cur = self.__head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def add(self, data):
        """在头部插入新的数据"""
        node = Node(data=data)
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, data):
        """在尾部追加新的节点"""
        node = Node(data=data)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, data):
        """在指定位置插入节点"""
        node = Node(data)
        if pos <= 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            index = 0
            cur = self.__head
            while index < pos - 1:
                index += 1
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, data):
        """移除指定元素"""
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                if cur is self.__head:
                    self.__head = cur.next
                    # 判断是否只有一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, data):
        """判断元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False
