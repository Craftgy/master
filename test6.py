import random
price=random.randint(1000,1500)
guess=int(input())
if guess>price:
    print('da')
elif guess<price:
    print('xiao')
else:
    print('right')