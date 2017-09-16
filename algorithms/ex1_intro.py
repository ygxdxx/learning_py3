#! python3

import time

# TODO 算法
# 独立存在的用于解决问题的方法和思路


# 1.如果 a + b + c = 1000，且a^2 + b^2 = c^2 (a,b,c为自然数)，求出a、b、c可能的组合
# v 1.0
"""
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if (a + b + c == 1000) and (a ** 2 + b ** 2 == c ** 2):
                print('a=%d b=%d c=%d：' % (a, b, c))
end_time = time.time()

print('Done! all time is %s' % (end_time - start_time))
"""

# v 1.1
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print('a=%d b=%d c=%d：' % (a, b, c))
end_time = time.time()
print('Done! all time is %s' % (end_time - start_time))


# TODO 时间复杂度 - 大O阶 O(n)
# 算法的执行效率与其所解决问题的规模有关系，即问题的数量级
# 关注算法执行效率的时候，只需要关注算法的主要数量级即可，忽略掉非重要的部分
# 例如，设T为时间，n为算法执行的步骤
# 则T1(n) = n^3 * 2 ≈ T2(n) = n^3 * 5，即 T1 = T2 = n^3 忽略了常数部分和系数部分
# 所以，要脱离机器环境也可以客观的描述算法的执行效率


# TODO 算法效率衡量
# 1. 最优时间复杂度 - 最少需要的基本操作数量
# 2. 最坏时间复杂度 - 最多需要的基本操作数量
# 3. 平均时间复杂度 - 平均需要的基本操作数量
# 通常关注最坏时间复杂度，因为最优只是最乐观的状态下，而平均则浮动较大难以估计


# TODO 计算复杂度
# 1. 基本操作：操作只有常数项 O(1)
# 2. 顺序结构：时间复杂度按照加法进行计算
# 3. 条件结构：对复杂度取最大值
# 4. 循环结构：时间复杂度按照乘法进行计算
# 最后进行计算的时候，只保留最高次项，对于常数项和系数都可以进行忽略

# TODO 常见时间复杂度的计算
# 步骤           阶数      术语
# 12            O(1)     常数阶
# 2n+3          O(n)     线性阶
# 3n^2+3        O(n^2)   平方阶
# 5log2n        O(logn)  对数阶
# 2n+3nlog2n    O(nlogn) nlogn阶
# 6n^3+2n^2+3n  O(n^3)   立方阶


# TODO 数据结构和算法的关系
# 数据结构描述了数据元素之间的关系
# 程序只需在数据结构的基础上设计和选择相应的算法
# 程序 = 数据结构 + 算法