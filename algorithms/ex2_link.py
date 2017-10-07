#! python3


class Node(object):
    """节点ADT"""

    def __init__(self, elem):
        self.elem = elem
        self.nxt = None


class SingleLink(object):
    """单链表"""

    def __init__(self, item=None):
        self._head = item

    def is_empty(self):
        """判断链表是否为空"""
        # 判断头节点是否为空
        return self._head is None

    def length(self):
        """返回链表长度"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.nxt
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem)
            cur = cur.nxt

    def add(self, item):
        """在链表头部添加节点"""
        pass

    def append(self, item):
        """在链表的尾部添加"""
        # 创建新的节点
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.nxt is not None:
                cur = cur.nxt
            cur.nxt = node

    def insert(self, pos, item):
        """在指定位置添加"""
        pass

    def remove(self, item):
        """删除指定元素"""
        pass

    def search(self, item):
        """判断元素是否存在"""
        pass


if __name__ == '__main__':
    ll = SingleLink()
    print(ll.length())
    print(ll.is_empty())

    # 追加元素
    ll.append('hello')
    print(ll.length())
    print(ll.is_empty())
    ll.append('hello')
    ll.append('hello')
    ll.append('hello')
    ll.append('hello')
    ll.append('hello')
    ll.append('hello')

    print(ll.length())
    print(ll.is_empty())
    ll.travel()
