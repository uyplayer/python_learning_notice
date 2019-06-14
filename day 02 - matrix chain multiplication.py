# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 23:10
# @Author  : UYPLAYER
# @Site    : uyplayer.com
# @File    : day 02 - matrix chain multiplication.py
# @Software: PyCharm

A=[[1,2,3],[4,5,6],[7,8,9]] # 3*3
B=[[2,1],[6,5],[6,9]] # 3*2
'''
a*b=>(3*2)
'''
c=[[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
print(c)

