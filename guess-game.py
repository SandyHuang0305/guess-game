#猜數字遊戲
import random

r = random.randint(1, 100)
count = 0
while True:
    count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
              print('你猜對了喔')
              break
    elif num > r:
              print('比答案大喔')
    elif num < r:
              print('比答案小喔')
    print('你已經猜了', count, '次了喔')	