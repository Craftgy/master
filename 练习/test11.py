import datetime
def inputdate():
    indate=input()
    indate=indate.strip()
    datestr=indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]
    return datetime.datetime.strptime(datestr,'%Y-%m-%d') 

if __name__ == "__main__":
    print('----------')
    sdate=inputdate()
    in_num=int(input('jiange'))
    fdate=sdate+datetime.timedelta(days=in_num)
    print('tuisuan'+str(fdate))