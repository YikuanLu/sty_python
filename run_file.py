# from collections import deque

# q = deque(maxlen=4)

# for i in range(4):
#     q.append(i+1)

# q.append(66)
# q.popleft()
# print(list(q))

# 找出几个最大/最小值
from heapq import nlargest, nsmallest

nums = [1, 2, 4, 7, 8, 45, -6]

maxs = nlargest(3, nums)
print(maxs)

mins = nsmallest(3, nums)
print(mins)
