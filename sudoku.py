import math
import os
import random
import re
import sys
import copy

def solved():
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                return False
    return True

def validnumbers(a,x,y):
    if(a[x][y]==0):
        b=[1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if a[x][i] in b:
                b.remove(a[x][i])
            if a[i][y] in b:
                b.remove(a[i][y])
        for i in range(3):
            for j in range(3):
                if a[3*(x//3)+i][3*(y//3)+j] in b:
                    b.remove(a[3*(x//3)+i][3*(y//3)+j])
        return b
    else:
        b=[0]
        return b
def findsingle():
    flag=False
    for i in range(9):
        for j in range(9):
            if len(hint[i][j])==1 and hint[i][j][0]!=0:
                removenumbers(hint[i][j][0],i,j)
                a[i][j]=hint[i][j][0]
                hint[i][j]=[0]
                flag=True
    return flag


def removenumbers(val,x,y):
    for i in range(9):
        if val in hint[x][i] and i!=y:
            hint[x][i].remove(val)
        if val in hint[i][y] and i!=x:
            hint[i][y].remove(val)
    for i in range(3):
        for j in range(3):
            if val in hint[3*(x//3)+i][3*(y//3)+j] and 3*(x//3)+i!=x and 3*(y//3)+j!=y:
                hint[3*(x//3)+i][3*(y//3)+j].remove(val)

def uniquenumber():
    flag=False
    for k in range(1,10):
        for i in range(9):
            count=0
            for j in range(9):
                if k in hint[i][j]:
                    count+=1
                    x,y=i,j
            if count==1:
                removenumbers(k,x,y)
                a[x][y]=k
                hint[x][y]=[0]
                flag=True
            count=0
            for j in range(9):
                if k in hint[j][i]:
                    count+=1
                    x,y=j,i
            if count==1:
                removenumbers(k,x,y)
                a[x][y]=k
                hint[x][y]=[0]
                flag=True
        
        for I in range(3):
            for J in range(3):
                count=0
                for i in range(3):
                    for j in range(3):
                        if k in hint[3*I+i][3*J+j]:
                            count+=1
                            x,y=3*I+i,3*J+j
                if count==1:
                    removenumbers(k,x,y)
                    a[x][y]=k
                    hint[x][y]=[0]
                    flag=True
    return flag

def guess():
    global hint,sol
    flag=False
    for i in range(9):
        for j in range(9):
            if len(hint[i][j])>1:
                flag=True
                h=copy.deepcopy(hint)
                for k in h[i][j]:
                    a[i][j]=k
                    removenumbers(k,i,j)
                    hint[i][j]=[0]
                    solve()
                    if solved():
                        print("")
                        for x in range(9):
                            for y in range(9):
                                print(a[x][y], end=" ")
                            print("")
                        sol=True
                    a[i][j]=0
                    hint=copy.deepcopy(h)
    return flag
                



def solve():
    if findsingle() or uniquenumber() or guess():
        if sol:
            return
        solve()
    return
    


a=[]
sol=False
for i in range(9):
    temp=[]
    temp=list(map(int, input().split()))
    a.append(temp)

hint=[]
for i in range(9):
    temp=[]
    for j in range(9):
        temp.append(validnumbers(a,i,j))
    hint.append(temp)

solve()

    

# print("")
# for i in range(9):
#     for j in range(9):
#         print(hint[i][j], end="")
#     print("")

print("")
for i in range(9):
    for j in range(9):
        print(a[i][j], end=" ")
    print("")

'''
2 4 0 0 0 7 0 0 0
1 8 9 0 0 0 2 7 5
5 0 3 0 0 1 4 0 0
0 1 0 0 2 0 0 0 7
0 0 7 0 0 0 0 2 0
9 5 0 0 0 0 3 4 0
7 0 4 0 0 2 8 9 1
3 0 0 0 0 8 0 5 0
8 0 5 7 1 4 6 0 0


3 0 0 2 0 1 4 6 0
0 9 0 0 5 8 0 0 3
0 2 0 7 0 0 0 0 0
6 0 1 0 0 0 8 0 7
0 0 2 0 1 0 0 9 0
0 3 0 8 0 4 0 0 6
9 0 4 0 7 0 5 8 0
0 7 0 0 0 0 0 0 9
8 0 0 0 4 6 0 3 0


0 5 2 0 0 0 3 7 0
0 0 9 2 0 6 8 0 1
0 0 8 3 7 0 0 0 0
0 0 0 0 0 4 0 5 9
0 9 0 0 6 0 4 2 0
2 0 0 8 0 0 0 0 3
0 0 0 0 3 7 5 0 2
6 0 5 9 0 8 1 0 0
0 7 0 0 0 0 9 6 0
 

0 2 0 0 0 4 3 0 0
9 0 0 0 2 0 0 0 8
0 0 0 6 0 9 0 5 0
0 0 0 0 0 0 0 0 1
0 7 2 5 0 3 6 8 0
6 0 0 0 0 0 0 0 0
0 8 0 2 0 5 0 0 0
1 0 0 0 9 0 0 0 3
0 0 9 8 0 0 0 6 0

0 0 0 4 0 0 0 8 0
1 9 0 6 0 0 4 5 0
0 2 0 0 8 0 0 0 0
0 0 0 0 0 0 0 9 7
0 0 2 0 0 0 6 0 0
8 1 0 0 0 0 0 0 0
0 0 0 0 7 0 0 6 0
0 7 3 0 0 5 0 1 9
0 4 0 0 0 9 0 0 0
'''