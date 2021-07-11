import time
import numpy as np

start = time.time()

# ls = [[1, 2, 3], [9, 8, 7]]

# npl = np.array(ls)

# print(npl)

# print('number of dim:', npl.ndim)
# print('shape:', npl.shape)
# print('size:', npl.size)

# a = np.array([1, 2, 3], dtype=np.int32)
# print(a.dtype)


def python_sum(n):
    a = [i**2 for i in range(n)]
    b = [i**3 for i in range(n)]
    c = []
    for x in range(n):
        c.append(a[x] + b[x])
    return c


def np_sum(n):
    a = np.array(range(n))**2
    b = np.array(range(n))**3
    c = a + b
    return c


count = 10
# python_sum(count)
nr = np_sum(count)
print(nr, nr.dtype)
end = time.time()

print('Running time: %s Seconds' % (end - start))
