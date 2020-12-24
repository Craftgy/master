def fun():
    num=int(input('qingshuru'))
    print(num,'deerjinzhi:',bin(num))
    print('\33[0:34 %sdeerjinzhi%s' % (num,bin(num)))
    
if __name__=='__main__':
    while True:
        try:
            fun()
            break
        except:
            print('eorro')
            fun()