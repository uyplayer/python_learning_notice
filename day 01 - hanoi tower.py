# -*- coding: utf-8 -*-
# @Time    : 19-5-31 下午6:07
# @Author  : UYPLAYER
# @Site    : uyplayer.com
# @github  : github.com/uyplayer
# @File    : day 01 - hanoi tower.py
# @Software: PyCharm

# 盘子从x移到z,y用于辅助
def hannoy(n,x,y,z):
    if n==1:
        print(x,"=>",z)
    else:
        hannoy(n-1,x,z,y)
        print(x, "=>", z)
        hannoy(n - 1, y, x, z)

if __name__=="__main__":
    hannoy(2,"A","B","C")