#! python3


def select_sort(lst):
    """选择排序"""
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]


if __name__ == '__main__':
    data = [17, 20, 93, 54, 77, 31, 44, 55, 226]
    print(data)
    select_sort(data)
    print(data)

