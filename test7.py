year=[82,76,87,00,98,87,00]
print('愿列表:',year)
for index,value in enumerate(year):
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print('xiugaihou',year)
year.sort()
print(year)
year.sort(reverse=True) 
print(year)