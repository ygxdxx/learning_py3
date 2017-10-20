#! python3


def bubble_sort(lst):
    """冒泡排序"""
    # 最坏情况 O(n^2)
    # 最优情况 O(n)
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_imp(lst):
    """冒泡排序优化"""
    # 最优情况 O(n)
    # 最坏情况 ???
    n = len(lst)
    for i in range(n - 1):
        # 用于标记是否已经完全有序
        flag = True
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                flag = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        # 判断当前是否已经完全有序
        if flag:
            break


if __name__ == '__main__':
    data = [3, 1, 5, 4, 2]
    print(data)
    bubble_sort(data)
    print(data)
