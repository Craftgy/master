import numpy as np
import matplotlib.pyplot as plt

#plt.plot() #画图
#plt.show() #显示图片

#x=np.linspace(-1,1,201)
#y=np.exp(-x**2/2)

#读取文件,返回数组 skiprow指跳过几行,delimiter确认分割符
data=np.loadtxt('/Users/craft/资料/python/master/数据分析/20201223EuCd2P2_70V.txt',skiprows=1,delimiter=',')

x= data[:,0]
y= data[:,1]

fig=plt.figure(figsize=[4,4])#创建并返回一个图片对象
sub=fig.add_subplot(111)# 行列位置

sub.plot(x,y)
#设置行列名字，大小
sub.set_xlabel('$x$',fontsize=16)
sub.set_ylabel('$y$',fontsize=16)
#设置子标题 sub.set_title(str):设置subplot标题
sub.set_title('$\Gamma$',fontsize=16)
#设置总标题
fig.suptitle('Figure 1',fontsize=20)
#fig.savefig('./figure1.png',dpi=500)
plt.show()
plt.close('all')#销毁内存
