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

def finddot(a):
    ran=[]
    for i in range(3):
        for j in range(3):
            if(a[i][j]=='.'):
                ran.append([i,j])
    return random.choice(ran)

def comp(a):
    for i in range(3):
        if(a[i][0]=="O"):
            if(a[i][1]=="O" and a[i][2]=="."):
                return [i,2]
            elif(a[i][1]=="." and a[i][2]=="O"):
                return [i,1]
        elif(a[i][0]=="." and a[i][1]=="O" and a[i][2]=="O"):
            return [i,0]


        if(a[0][i]=="O"):
            if(a[1][i]=="O" and a[2][i]=="."):
                return [2,i]
            elif(a[1][i]=="." and a[2][i]=="O"):
                return [1,i]
        elif(a[0][i]=="." and a[1][i]=="O" and a[2][i]=="O"):
            return [0,i]


    if(a[0][0]=="O"):
        if(a[1][1]=="O" and a[2][2]=="."):
            return [2,2]
        elif(a[1][1]=="." and a[2][2]=="O"):
            return [1,1]
    elif(a[0][0]=="." and a[1][1]=="O" and a[2][2]=="O"):
        return [0,0]


    if(a[0][2]=="O"):
        if(a[1][1]=="O" and a[0][2]=="."):
            return [0,2]
        elif(a[1][1]=="." and a[0][2]=="O"):
            return [1,1]
    elif(a[0][2]=="." and a[1][1]=="O" and a[2][0]=="O"):
        return [0,2]


    for i in range(3):
        if(a[i][0]=="X"):
            if(a[i][1]=="X" and a[i][2]=="."):
                return [i,2]
            elif(a[i][1]=="." and a[i][2]=="X"):
                return [i,1]
        elif(a[i][0]=="." and a[i][1]=="X" and a[i][2]=="X"):
            return [i,0]


        if(a[0][i]=="X"):
            if(a[1][i]=="X" and a[2][i]=="."):
                return [2,i]
            elif(a[1][i]=="." and a[2][i]=="X"):
                return [1,i]
        elif(a[0][i]=="." and a[1][i]=="X" and a[2][i]=="X"):
            return [0,i]
        

    if(a[0][0]=="X"):
        if(a[1][1]=="X" and a[2][2]=="."):
            return [2,2]
        elif(a[1][1]=="." and a[2][2]=="X"):
            return [1,1]
    elif(a[0][0]=="." and a[1][1]=="X" and a[2][2]=="X"):
            return [0,0]


    if(a[0][2]=="X"):
        if(a[1][1]=="X" and a[0][2]=="."):
            return [0,2]
        elif(a[1][1]=="." and a[0][2]=="X"):
            return [1,1]
    elif(a[0][2]=="." and a[1][1]=="X" and a[2][0]=="X"):
        return [0,2]
    
    

    return finddot(a)


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
    b=comp(a)
    x, y=b[0], b[1]
    print("Computer's turn: "+str(x+1)+" "+str(y+1))
        
    a[x][y]="O"
    if winorlose(a,"O"):
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print("")
        print("Computer wins!!!")
        break   
    if(nodot(a)):
        print("It's a draw!!!")
        break