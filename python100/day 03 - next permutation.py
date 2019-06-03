# -*- coding: utf-8 -*-
# @Time    : 19-6-3 上午8:33
# @Author  : UYPLAYER
# @Site    : uyplayer.com
# @github  : github.com/uyplayer
# @File    : day 03 - next permutation.py
# @Software: PyCharm

#排序
def permute(values):
    n = len(values)

    # i: position of pivot
    for i in reversed(range(n - 1)):
        print (i)
        if values[i] < values[i + 1]:
            break
    else:
        # very last permutation
        values[:] = reversed(values[:])
        return values

    # j: position of the next candidate
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            # swap pivot and reverse the tail
            values[i], values[j] = values[j], values[i]
            values[i + 1:] = reversed(values[i + 1:])
            break

    return values

permute([4, 3, 2, 1])
