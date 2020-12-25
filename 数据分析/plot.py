#----------------------------------------------------#
#龚毅
#年份：12.25    时间：10:40
#-----------------------------------------------------
#版本 1.0.1
#取消了需要输入个数，按输入路径个数获取文件数
#-----------------------------------------------------
#问题：标题不显示
import numpy as np
import matplotlib.pyplot as plt
#定义文件个数
#number=int(input('请输入文件个数：'))
x=[]
y=[]
dataname=[]
name=[]
number=0;
for i in range(100):
    #print('请输入第%d文件路径：'%(i+1))
    dataname.append(input('请输入第%d个文件路径（输入N结束）：'%(i+1)))
    if dataname[i]=='N':
        break
    else:
        number=number+1
#输入文件并初始化
for i in range(number):
    # #print('请输入第%d文件路径：'%(i+1))
    # dataname.append(input('请输入第%d个文件路径：'%(i+1)))
    data=np.loadtxt(dataname[i])
    x.append(data[:,0])
    y.append(data[:,1])

#创建表格
fig=plt.figure(figsize=[8,8])
sub=fig.add_subplot(111)
sub.set_title('T-R',fontsize=14)
#fig.suptitle(r'$样品$',fontsize=15)

#设定名字
for i in range(number):
    name.append(input('请输入第%d个图例名字:'%(i+1)))
    sub.plot(x[i],y[i],label=name[i])
sub.legend(fontsize=12)

#设置坐标名字
sub.set_xlabel(r'$T$',fontsize=14)
sub.set_ylabel(r'$R$',fontsize=14)

#设置坐标刻度
sub.set_xticks(np.arange(0,30.1,5))
sub.set_xticks(np.arange(0,30.1,1),minor=True)
#sub.set_yticks(np.arange(0,10000000000.1,10000000))
#sub.set_yticks(np.arange(0,10000000000.1,100000),minor=True)

#设置网格
sub.grid(axis='both',which='both',linestyle='--')

plt.show()
plt.close(all)
