   data=np.loadtxt(dataname[i])
#     x.append(data[:,0])
#     x.append(data[:,0])

# #创建表格
# fig=plt.figure(figsize=[16,16])
# sub=fig.add_subplot(111)
# sub.set_title('T-R',fontsize=14)
# fig.suptitle('样品',fontsize=15)

# #设定名字
# for i in range(number):
#     name.append('请输入图例名字:')
#     sub.plot(x[i],y[i],label=name[i])
# sub.legend(fontsize=12)

# #设置坐标名字
# sub.set_xlabel(r'$T$',fontsize=14)
# sub.set_ylabel(r'$R$',fontsize=14)

# #设置坐标刻度
# sub.set_xticks(np.arange(0,30.1,5))
# sub.set_xticks(np.arange(0,30.1,1),minor=True)
# sub.set_yticks(np.arange(0,100000000.1,10000000))
# sub.set_yticks(np.arange(0,100000000.1,100000),minor=True)

# #设置网格
# sub.grid(axis='both',which='both',linestyle='--')

# plt.show()
# plt.close(all)
