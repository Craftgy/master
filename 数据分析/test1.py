import numpy as np

'''
#method1
arr1 = np.zeros(5) #创建元素都为0的数组
arr2 = np.zeros([5,3],dtype=int)
print('arr1=',arr1)
print('arr2=',arr2)
'''
'''
#method2
arr1=np.array([0,1,2]) #直接创建数组
arr2=np.array([ [0,1,2],[3,2,1],[-1,-2,-3] ])
print('arr1=',arr1)
print('arr2=',arr2)
print(arr2.shape,arr2.shape[0],arr2.shape[1])#返回数组形状
'''
'''
#method 3
arr1=np.arange(0,10.001,0.5) #创建数组 初值，末值，步长
print(arr1)
'''
'''
#method 4
arr1=np.linspace(0,10,21,endpoint=False) #初值，末值，长度,是否包含结束值
print('arr1=',arr1)
'''

#Numpy array can be of more types

arr=np.array(['name',1,2,5,0],dtype=object)
print(arr)