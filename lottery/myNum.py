# -*-encoding:utf-8 -*-

# File: myNum
# Author: Administrator
# CreateTime: 2022/4/10 11:05

import random

def getNum(num):
    setn = set()
    while True:
        result = random.randint(1, num)
        setn.add(result)
        if len(setn) == 5 and num == 35:
            break
        if len(setn) == 2 and num == 12:
            break
    return setn

def main():
    x = [9, 10]
    for i in range(100):
        if i in x:
            print(getNum(35), getNum(12))

if __name__ == '__main__':
    main()
