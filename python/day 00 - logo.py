# -*- coding: utf-8 -*-
# @Time    : 19-5-31 上午9:02
# @Author  : UYPLAYER
# @Site    : uyplayer.com
# @github  : github.com/uyplayer
# @File    : day 00 - logo.py
# @Software: PyCharm

# lib
import numpy as np
from bokeh.plotting import figure, show, output_notebook

# algorithm
xs,ys,cs = [],[],[]

for x in range(0,30):
    for y in range(0,30):
        up=np.random.randint(0,2)
        xs.append([x,x+8])
        '''
        if condition:(up>=.5) 
        '''
        ys.append([y+.8*(up>=.5),y+.8*(up<.5)])
        col = np.random.randint(0,4)
        cs.append({0:"blue",1:"red",2:"white",3:"white"}[col])

# plot
output_notebook()

plot=figure(plot_width=800,plot_height=800)
plot.grid.visible = False
plot.xaxis.visible = False
plot.yaxis.visible = False

plot.multi_line(xs,ys,color=cs,line_width=6,line_alpha=.1,line_cap='round')
plot.multi_line(xs, ys, color='black')

