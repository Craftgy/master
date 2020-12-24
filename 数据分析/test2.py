import numpy as np
import pandas as pd

#create apandas dateframe

#arr= np.array([['zhang',60,90],['Li',80,70],['Wang',100,50]])

#arr=dict({'name':['zhang','li','wang'],'math':[60,80,90],'english':[90,100,20]})

#DateFrame 输出列表：列表，数轴标签，横轴标签
#df=pd.DataFrame(arr,index=[1,2,3],columns=['name','math','english'])

#csv读取
df=pd.read_csv('/Users/craft/资料/python/master/数据分析/data.csv')
#改变竖列标号
df.index=[1,2,3]

#df.loc[]:根据index选取某一行数据
#   print(df.loc[3])
#df[column name]:选取某一列
#   print(df['name'])
#   print(df.name)

#添加一列
df['total']=df.math+df.english
#   print(df)

#df.sort_values():根据某一（多）列排序
#   print(df.sort_values(by='english',ascending=False))#排序
#检索
print(df[df.name=='wang'])
