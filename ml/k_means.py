#! pythoy3

import numpy as npy


# 三个函数为辅助函数
def load_dataset(filename):
    """
    加载数据源
    """
    data_mat = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            curr_line = line.strip().split('\t')
            float_line = map(float, curr_line)
            data_mat.append(float_line)
    # 其中包含许多其他列表，成为一个矩阵
    return data_mat


def calc_dist(vec_a, vec_b):
    """
    计算两个向量的欧式距离
    """
    return npy.sqrt(npy.sum(npy.power(vec_a - vec_b, 2)))


def rand_cent(data_set, k):
    """
    为给定数据集构建一个包含k个随机质心的集合，要确保质心出现在边界范围之内
    """
    # 获取每个维度的数组中元素的个数
    n = npy.shape(data_set)[1]
    # 返回一个k维 每个维度包含n个元素的用0填充的数组
    # 并通过mat转换为矩阵matrix
    # TODO mat与array之间的区别？
    centroids = npy.mat(npy.zeros((k, n)))
    for index in range(n):
        # 获取矩阵当前列的中元素的最小值
        min_curr = npy.min(data_set[:, index])
        # 获取当前列的取值范围
        range_curr = float(npy.max(data_set[:, index]) - min_curr)
        # 生成质心并添加到矩阵当中
        centroids[:, index] = min_curr + range_curr * npy.random.rand(k, 1)

# mat = npy.array([[1, 2, 3], [4, 5, 6]])
# print(mat)
# print(mat[0:1, 0])
# print(mat.shape)
