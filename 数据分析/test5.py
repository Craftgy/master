import numpy as np
import matplotlib.pyplot as plt 

x=np.linspace(0,1,100)
y=10*x
y2=8*x
y3=10-5*x
fig=plt.figure()
sub=fig.add_subplot(111)
#多个图例添加
line1,=sub.plot(x,y,label=r'$y=10x$')
line2,=sub.plot(x,y2,label=r'$y=8$')
line3,=sub.plot(x,y3,label=r'$y=10-5x$')
#指定位置添加线
sub.axhline(y=4,color='red')
sub.axvline(x=0.8,color='bule',linestyle='-.') 


leg1=sub.legend(handles=[line1,line3],labels=['line1','line2'])#图例,字体，位置loc=[0.1,0.1]
sub.add_artist(leg1)
sub.legend(handles=[line2],loc=8)
#sub.legend(fontsize=12,loc='center left')#图例,字体，位置loc=[0.1,0.1]
sub.set_xlabel(r'$x$',fontsize=14)
sub.set_ylabel(r'$y$',fontsize=14)
#设置坐标
sub.set_xticks([0,0.5,1.0])
sub.set_xticks(np.arange(0,1.01,0.1),minor=True)
#_xticklabels(['a','b','c'])
#设置网格 axis='x' or 'y' or 'both' which='major' or 'minor' or 'both'
sub.grid(axis='both',which='both',linestyle='--')
#设置刻度   in inout out  pad 刻度和标签的距离 标签字体颜色labelsize=13,labelcolor='C1'
#top,bottom,left,right=True or False
#labeltop,left....  labelrotation=45 标签倾斜角度  grid_color 网格颜色 gird_linewidth gird_linstyle  网格透明度grid_alpha=0.5
sub.tick_params(axis='x',which='major',direction='in',pad =10,length=5,width=5,colors='C1',top=True,labelrotation=45)
plt.show()
plt.close(fig)