# from collections import deque

# q = deque(maxlen=4)

# for i in range(4):
#     q.append(i+1)

# q.append(66)
# q.popleft()
# print(list(q))

# 找出几个最大/最小值
# from heapq import heapify

# nums = [1, 2, 4, 7, 8, 45, -6]

# maxs = nlargest(3, nums)
# print(maxs)

# mins = nsmallest(3, nums)
# print(mins)

# heapify(nums)
# print(nums)
# d = {}
# d.setdefault('a', []).append(1)
# d['a'] = []
# d['a'].append(1)
# print(d)

# import os
# print(os.getcwd())

# import math
# print(math.pi / 4)

# import numpy as np
# n = np.eye(4)
# print(n)

map01 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
map02 = {'a': 1, 'bb': 10, 'cc': 3, 'd': 5}
# Find (key,value) pairs in common
print(map01.items() & map02.items())
