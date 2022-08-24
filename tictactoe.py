import math
import os
import random
import re
import sys

def winorlose(a, x):
    for i in range(3):
        if(a[i][0]==x and a[i][1]==x and a[i][2]==x):
            return True
        if(a[0][i]==x and a[1][i]==x and a[2][i]==x):
            return True
    if((a[0][0]==x and a[1][1]==x and a[2][2]==x) or (a[0][2]==x and a[1][1]==x and a[2][0]==x)):
        return True
    return False

def nodot(a):
    for i in range(3):
        for j in range(3):
            if(a[i][j]=='.'):
                return False
    return True


a=[['.','.','.'],['.','.','.'],['.','.','.']]
while True:
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=" ")
        print("")
    while(True):
        print("Player 1's turn: ", end="")
        x, y=map(int, input().split())
        if(a[x-1][y-1]=="."):
            break
        print("Please give a valid entry!!\nYou can't over write the previous moves")
    a[x-1][y-1]="X"
    if winorlose(a,"X"):
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print("")
        print("Player 1 wins!!!")
        break
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=" ")
        print("")
    if(nodot(a)):
        print("It's a draw!!!")
        break
    while(True):
        print("Player 2's turn: ", end="")
        x, y=map(int, input().split())
        if(a[x-1][y-1]=="."):
            break
        print("Please give a valid entry!!\nYou can't over write the previous moves")
    a[x-1][y-1]="O"
    if winorlose(a,"O"):
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print("")
        print("Player 2 wins!!!")
        break   
    if(nodot(a)):
        print("It's a draw!!!")
        break

