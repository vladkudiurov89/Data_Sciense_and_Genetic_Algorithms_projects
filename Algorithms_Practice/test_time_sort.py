import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


def selection(arrayToSort):
    a = arrayToSort.copy()
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a


def insertion(arrayToSort):
    a = arrayToSort.copy()
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
    return a


def bubble(arrayToSort):
    a = arrayToSort.copy()
    for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
    return a


def np_sort(arrayToSort):
    a = arrayToSort.copy()
    return np.sort(a)


def py_sorted(arrayToSort):
    a = arrayToSort.copy()
    return sorted(a)

res = pd.DataFrame(
    index=['selection', 'insertion', 'bubble', 'py_sorted', 'np_sort'],
    columns=np.logspace(2, 5, 4).astype(int),
    dtype=float
)

for j in res.columns:
    a = np.random.choice(j, j, replace=False)
    for i in res.index:
        stmt = '{}(a)'.format(i)
        setp = 'from __main__ import a, {}'.format(i)
        print('processing [{}]\tarray size: {}'.format(i,j), end='')
        res.at[i, j] = timeit.timeit(stmt, setp, number=50)
        print('\t\ttiming:\t{}'.format(res.at[i, j]))
print(res)

plt.figure()
ax = res.T.plot(loglog=True, style='-o', figsize=(10,8))
ax.set_xlabel('array size')
ax.set_ylabel('time (sec)')
plt.savefig('c:/temp/result.png')