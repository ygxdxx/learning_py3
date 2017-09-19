#! python3

import redis

# TODO Redis使用
# 连接方式
# 连接池
# 操作
#   1.String 操作
#   2.Hash 操作
#   3.List 操作
#   4.Set 操作
#   5.Sort Set 操作
# 管道
# 发布订阅

# 1.String操作
r = redis.Redis(host='127.0.0.1', port=6379)
# TODO 此处包含各种set方法
r.set('foo', 'bar')
print(r.get('foo').decode('utf-8'))

# 2.Hash操作


