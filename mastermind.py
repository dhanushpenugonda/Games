import math
import os
import random
import re
import sys

s
print("Code maker, you enter any 4 values from the numbers in range [1,6] and repitation is allowed")
cm=input("Enter your code: ")
attempts=int(input("Enter no of attempts you give to crack: "))
print("\n\n\n\n\n\n\n\n\n\n\n")
print("Code breaker, break the code!!")
print("YOU HAVE "+str(attempts)+" TRIES MORE!!!")
while attempts:
    while True:
        cb=input("Enter your guess: ")
        if len(cb)==4:
            break
        print("Enter 4 values only!!!")
    r,w=0,0
    for i in range(4):
        if(cm[i]==cb[i]):
            r+=1
        if cm[i] in cb:
            w+=1
    w-=r
    print(str(r)+"R "+str(w)+"W")
    if r==4:
        print("Code breaker, you cracked the code!!")
        break
    attempts-=1
    print("YOU HAVE "+attempts+" TRIES MORE!!!")