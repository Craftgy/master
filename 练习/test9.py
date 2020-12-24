def get_conut(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
    return count

if __name__=='__main__':
    s='hellpython,heeljava,hellogo'
    ch=input('dddd')
    count=get_conut(s,ch)
    print(f'{ch}zai{s}zhongchuxian:{count}')
    