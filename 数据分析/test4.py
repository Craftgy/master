import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#读取excel

df=pd.read_excel('/Users/craft/资料/python/master/数据分析/20201223EuCd2P2_70V.xlsx',sheet_name='Sheet1')
x=np.linspace(0,10,100)
y=np.exp(x)
#plot
fig=plt.figure()
sub=fig.add_subplot(111)

#传入x和y linewidth 线宽 ，linestyle  线条类型
#直线- 虚线 -- 虚点-. 点线‘ 不显示none,marker数据点 圆圈O 方块s 五角星* 上三角^
sub.plot(df['x'],df['y'],color='C1',linewidth=0.5,linestyle='--',marker='o')
#sub.plot(df['x'],df['y'],color='C1')
#颜色plt.cm
#sub.plot(x,y)
#sub.set_yscale('log',basey=10)#底数
sub.set_xlabel(r'$x$',fontsize=14)
sub.set_ylabel(r'$y$',fontsize=14)
sub.set_title(r'Plot 1',fontsize=14)
fig.suptitle(r'Figure 1',fontsize=15)
plt.show()
plt.close(all)

