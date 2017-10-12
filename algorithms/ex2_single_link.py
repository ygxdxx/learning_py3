#! python3


class Node(object):
    """节点ADT"""

    def __init__(self, elem):
        self.elem = elem
        self.nxt = None


class SingleLink(object):
    """单链表"""

    def __init__(self, item=None):
        self.__head = item

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.nxt
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.nxt

    def add(self, data):
        """在链表头部添加节点"""
        node = Node(data)
        node.nxt = self.__head
        self.__head = node

    def append(self, data):
        """在链表的尾部添加"""
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.nxt is not None:
                cur = cur.nxt
            cur.nxt = node

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
        prev = None
        cur = self.__head
        while cur is not None:
            if data == cur.elem:
                if cur == self.__head:
                    self.__head = cur.nxt
                else:
                    prev.nxt = cur.nxt
                break
            else:
                prev = cur
                cur = cur.nxt

    def search(self, data):
        """判断元素是否存在"""
        cur = self.__head
        while cur is not None:
            if data == cur.elem:
                return True
            else:
                cur = cur.nxt
        return False


if __name__ == '__main__':
    ll = SingleLink()
    print(ll.length())
    print(ll.is_empty())

    # 追加元素
    ll.append('0')
    print(ll.length())
    print(ll.is_empty())
    ll.append('1')
    ll.append('2')
    ll.append('3')
    ll.append('4')
    ll.append('5')
    ll.append('6')
    ll.insert(2, '101')
    ll.remove('2')

    ll.travel()
