#! python3


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleCycleLink(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node
        # 头节点存在则进行连接
        if node:
            node.nxt = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur.nxt is not self.__head:
            count += 1
            cur = cur.nxt
        return count

    def travel(self):
        """遍历链表"""
        # 链表为空的情况
        if self.is_empty():
            return None
        cur = self.__head
        while cur.nxt is not self.__head:
            print(cur.elem, end=' ')
            cur = cur.nxt
        # 每次next最后会少计算一个尾节，因此 退出循环的时候需要打印一下尾节点的元素
        print(cur.elem)

    def add(self, data):
        """在链表头部添加节点"""
        node = Node(data)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, data):
        """在链表的尾部添加"""
        node = Node(data)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, data):
        """
        在指定位置添加
        :param data: 插入的数据
        :param pos: 从0开始
        """
        if pos <= 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            count = 0
            prev = self.__head
            node = Node(data)
            while count < pos - 1:
                prev = prev.nxt
                count += 1
            node.nxt = prev.nxt
            prev.nxt = node

    def remove(self, data):
        """删除指定元素"""
        # 空列表
        if self.is_empty():
            return
        prev = None
        cur = self.__head
        while cur.next is not self.__head:
            if data == cur.data:
                if cur == self.__head:
                    # 头节点
                    tail = self.__head
                    while tail.next is not self.__head:
                        tail = tail.next
                    self.__head = cur.nxt
                    tail.next = self.__head
                else:
                    # 中间节点
                    prev.nxt = cur.nxt
                break
            else:
                prev = cur
                cur = cur.nxt
        # 尾节点
        if cur.data == data:
            # 只有一个节点
            if cur == self.__head:
                self.__head = None
            else:
                prev.next = cur.next

    def search(self, data):
        """判断元素是否存在"""
        cur = self.__head
        # 先判断是否为空
        if self.is_empty():
            return False
        while cur.next is not self.__head:
            if cur.data == data:
                return True
            else:
                cur = cur.nxt
        # 退出循环时候处于最后一个节点
        if cur.data == data:
            return True
        return False
