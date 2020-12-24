import numpy as np
import matplotlib.pyplot as plt
import datetime

x=np.sin(2*np.pi*np.arange(0,25)/24)
dt0=datetime.datetime(2020,5,10,0,30)
dt1=dt0+datetime.timedelta(days=1,minutes=1)

dt_arr=(np.arange(dt0,dt1,datetime.timedelta(hours=1))).astype(object)
fig=plt.figure()
sub=fig.add_subplot(111)
sub.plot(dt_arr,x)

sub.set_xlabel('time',fontsize=15)
sub.set_ylabel(r'$x$',fontsize=15)

xticks=(np.arange(dt0,dt1,datetime.timedelta(hours=6))).astype(object)
sub.set_xticks(xticks)
xticks_minor=(np.arange(dt0,dt1,datetime.timedelta(hours=1))).astype(object)
sub.set_xticks(xticks_minor,minor=True)
#子刻度
xticklabels = np.zeros(len(xticks),dtype=object)
for i in range(len(xticks)):
    xticklabels[i]=xticks[i].strftime('%H:%M')
sub.set_xticklabels(xticklabels)
sub.set_title(r'Temperature on'+dt0.strftime('%Y-%m-%d'),fontsize=15)

plt.show()
plt.close(all)
# dt=datetime.datetime(2020,5,9, 15 ,51, 45, 10000)
# #print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,dt.microsecond)
# dt0=datetime.datetime(2020,1,1,0,0)
# delta_t=dt-dt0
# print(delta_t)
# print(delta_t.days)
# print(delta_t.total_seconds())
#delta_t=datetime.timedelta(hours=3,minutes=6,seconds=45)
#print(dt+delta_t)
#可以比大小
#dt_str=dt.strftime('%y-%m-%d %H:%M:%S')
# print(str_dt)
# dt_str='05/10/20--20:45:51.01000'
# dt1=datetime.datetime.strptime(dt_str,'%m/%d/%y--%H:%M:%S.%f')
# print(dt1)
