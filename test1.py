fp=open('/Users/craft/Desktop/test.txt','w')
print('你是个🐷吧',file=fp)
fp.close()


with open('test2.txt','w') as file:
    file.write('你是个🐰吧')
