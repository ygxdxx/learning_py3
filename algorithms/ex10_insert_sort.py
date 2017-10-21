#! python3


def insert_sort(lst):
    """插入排序"""
    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break


if __name__ == '__main__':
    data = [17, 20, 93, 54, 77, 31, 44, 54, 226]
    print(data)
    insert_sort(data)
    print(data)
