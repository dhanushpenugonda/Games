import math
import os
import random
import re
import sys

def checkforlegalmoves(x,y):
    for i in range(8):
        for j in range(8):
            if a[i][j]==x:
                if j+1<=7:
                    if a[i][j+1]==y:
                        k=2
                        while j+k<=7:
                            if a[i][j+k]==".":
                                return True
                            elif a[i][j+k]==x:
                                break
                            k+=1
                if i+1<=7:
                    if a[i+1][j]==y:
                        k=2
                        while i+k<=7:
                            if a[i+k][j]==".":
                                return True
                            elif a[i+k][j]==x:
                                break
                            k+=1

                if j-1>=0:
                    if a[i][j-1]==y:
                        k=2
                        while j-k>=0:
                            if a[i][j-k]==".":
                                return True
                            elif a[i][j-k]==x:
                                break
                            k+=1
                if i-1>=7:
                    if a[i-1][j]==y:
                        k=2
                        while i-k>=0:
                            if a[i-k][j]==".":
                                return True
                            elif a[i-k][j]==x:
                                break

                    
                if j+1<=7 and i+1<=7:
                    if a[i+1][j+1]==y:
                        k=2
                        while i+k<=7 and j+k<=7:
                            if a[i+k][j+k]==".":
                                return True
                            elif a[i+k][j+k]==x:
                                break
                            k+=1
                if i+1<=7 and j-1>=0:
                    if a[i+1][j-1]==y:
                        k=2
                        while i+k<=7 and j-k>=0:
                            if a[i+k][j-k]==".":
                                return True
                            elif a[i+k][j-k]==x:
                                break
                            k+=1

                if j-1>=0 and i-1>=0:
                    if a[i-1][j-1]==y:
                        k=2
                        while i-k>=0 and j-k>=0:
                            if a[i-k][j-k]==".":
                                return True
                            elif a[i-k][j-k]==x:
                                break
                            k+=1
                if i-1>=7 and j+1<=7:
                    if a[i-1][j+1]==y:
                        k=2
                        while i-k>=0 and j+k<=7:
                            if a[i-k][j+k]==".":
                                return True
                            elif a[i-k][j+k]==x:
                                break
                            k+=1
    return False

def validornot(x,y,k,l):
    if y+1<=7:
        if a[x][y+1]==l:
            i=2
            while y+i<=7:
                if a[x][y+i]==k:
                    return True
                elif a[x][y+i]==".":
                    break
                i+=1
    if y-1>=0:
        if a[x][y-1]==l:
            i=2
            while y-i>=0:
                if a[x][y-i]==k:
                    return True
                elif a[x][y-i]==".":
                    break
                i+=1
    if x+1<=7:
        if a[x+1][y]==l:
            i=2
            while x+i<=7:
                if a[x+i][y]==k:
                    return True
                elif a[x+i][y]==".":
                    break
                i+=1
    if x-1>=0:
        if a[x-1][y]==l:
            i=2
            while x-i>=0:
                if a[x-i][y]==k:
                    return True
                elif a[x-i][y]==".":
                    break
                i+=1
    
    
    if y+1<=7 and x+1<=7:
        if a[x+1][y+1]==l:
            i=2
            while y+i<=7 and x+i<=7:
                if a[x+i][y+i]==k:
                    return True
                elif a[x+i][y+i]==".":
                    break
                i+=1
    if y-1>=0 and x+1<=7:
        if a[x+1][y-1]==l:
            i=2
            while y-i>=0 and x+i<=7:
                if a[x+i][y-i]==k:
                    return True
                elif a[x+i][y-i]==".":
                    break
                i+=1
    if y-1>=0 and x-1>=0:
        if a[x-1][y-1]==l:
            i=2
            while y-i>=0 and x-i>=0:
                if a[x-i][y-i]==k:
                    return True
                elif a[x-i][y-i]==".":
                    break
                i+=1
    if y+1<=7 and x-1>=0:
        if a[x-1][y+1]==l:
            i=2
            while y+i<=7 and x-i>=0:
                if a[x-i][y+i]==k:
                    return True
                elif a[x-i][y+i]==".":
                    break
                i+=1
    return False
    
def swap(x,y,k,l):
    a[x][y]=k
    li=[-100,-100]
    if y+1<=7:
        if a[x][y+1]==l:
            i=2
            while y+i<=7:
                if a[x][y+i]==k:
                    li[0],li[1]=x,y+i
                    break
                elif a[x][y+i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=0
        while y+i!=li[1]:
            a[x][y+i]=k
            i+=1
        
    li=[-100,-100]
    if y-1>=0:
        if a[x][y-1]==l:
            i=2
            while y-i>=0:
                if a[x][y-i]==k:
                    li[0],li[1]=x,y-i
                    break
                elif a[x][y-i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while y-i!=li[1]:
            a[x][y-i]=k
            i+=1

    li=[-100,-100]
    if x+1<=7:
        if a[x+1][y]==l:
            i=2
            while x+i<=7:
                if a[x+i][y]==k:
                    li[0],li[1]=x+i,y
                    break
                elif a[x+i][y]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while x+i!=li[0]:
            a[x+i][y]=k
            i+=1

    li=[-100,-100]
    if x-1>=0:
        if a[x-1][y]==l:
            i=2
            while x-i>=0:
                if a[x-i][y]==k:
                    li[0],li[1]=x-i,y
                    break
                elif a[x-i][y]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while x-i!=li[0]:
            a[x-i][y]=k
            i+=1
        

    li=[-100,-100]
    if y+1<=7 and x+1<=7:
        if a[x+1][y+1]==l:
            i=2
            while y+i<=7 and x+i<=7:
                if a[x+i][y+i]==k:
                    li[0],li[1]=x+i,y+i
                    break
                elif a[x+i][y+i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while y+i!=li[1]:
            a[x+i][y+i]=k
            i+=1

    li=[-100,-100]
    if y-1>=0 and x+1<=7:
        if a[x+1][y-1]==l:
            i=2
            while y-i>=0 and x+i<=7:
                if a[x+i][y-i]==k:
                    li[0],li[1]=x+i,y-i
                    break
                elif a[x+i][y-i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while y-i!=li[1]:
            a[x+i][y-i]=k
            i+=1

    li=[-100,-100]
    if y-1>=0 and x-1>=0:
        if a[x-1][y-1]==l:
            i=2
            while y-i>=0 and x-i>=0:
                if a[x-i][y-i]==k:
                    li[0],li[1]=x-i,y-i
                    break
                elif a[x-i][y-i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while y-i!=li[1]:
            a[x-i][y-i]=k
            i+=1
        
    li=[-100,-100]
    if y+1<=7 and x-1>=0:
        if a[x-1][y+1]==l:
            i=2
            while y+i<=7 and x-i>=0:
                if a[x-i][y+i]==k:
                    li[0],li[1]=x-i,y+i
                    break
                elif a[x-i][y+i]==".":
                    break
                i+=1
    if li!=[-100,-100]:
        i=1
        while y+i!=li[1]:
            a[x-i][y+i]=k
            i+=1

def count():
    c0,c1=0,0
    for i in range(8):
        for j in range(8):
            if a[i][j]==0:
                c0+=1
            elif a[i][j]==1:
                c1+=1
    return [c0,c1]

def comp(x,y):
    li=[]
    for i in range(8):
        for j in range(8):
            if a[i][j]==x:
                if j+1<=7:
                    if a[i][j+1]==y:
                        k=2
                        while j+k<=7:
                            if a[i][j+k]==".":
                                li.append([i,j+k])
                                break
                            elif a[i][j+k]==x:
                                break
                            k+=1
                if i+1<=7:
                    if a[i+1][j]==y:
                        k=2
                        while i+k<=7:
                            if a[i+k][j]==".":
                                li.append([i+k,j])
                                break
                            elif a[i+k][j]==x:
                                break
                            k+=1

                if j-1>=0:
                    if a[i][j-1]==y:
                        k=2
                        while j-k>=0:
                            if a[i][j-k]==".":
                                li.append([i,j-k])
                                break
                            elif a[i][j-k]==x:
                                break
                            k+=1
                if i-1>=7:
                    if a[i-1][j]==y:
                        k=2
                        while i-k>=0:
                            if a[i-k][j]==".":
                                li.append([i-k,j])
                                break
                            elif a[i-k][j]==x:
                                break

                    
                if j+1<=7 and i+1<=7:
                    if a[i+1][j+1]==y:
                        k=2
                        while i+k<=7 and j+k<=7:
                            if a[i+k][j+k]==".":
                                li.append([i+k,j+k])
                                break
                            elif a[i+k][j+k]==x:
                                break
                            k+=1
                if i+1<=7 and j-1>=0:
                    if a[i+1][j-1]==y:
                        k=2
                        while i+k<=7 and j-k>=0:
                            if a[i+k][j-k]==".":
                                li.append([i+k,j-k])
                                break
                            elif a[i+k][j-k]==x:
                                break
                            k+=1

                if j-1>=0 and i-1>=0:
                    if a[i-1][j-1]==y:
                        k=2
                        while i-k>=0 and j-k>=0:
                            if a[i-k][j-k]==".":
                                li.append([i-k,j-k])
                                break
                            elif a[i-k][j-k]==x:
                                break
                            k+=1
                if i-1>=7 and j+1<=7:
                    if a[i-1][j+1]==y:
                        k=2
                        while i-k>=0 and j+k<=7:
                            if a[i-k][j+k]==".":
                                li.append([i-k,j+k])
                                break
                            elif a[i-k][j+k]==x:
                                break
                            k+=1

    
    return random.choice(li)

    

a=[]
for i in range(8):
    temp=[]
    for j in range(8):
        temp.append(".")
    a.append(temp)
a[3][3],a[3][4],a[4][3],a[4][4]=1,0,0,1
print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
for i in range(8):
    print("["+str(i+1)+"]", end="  ")
    for j in range(8):
        print(a[i][j], end="   ")
    print("\n")

while True:
    if(checkforlegalmoves(1,0)):
        while True:
            p1,p2=0,0
            while True:
                try:
                    x,y=map(int,input("Player 1's turn(1): ").split())
                    break
                except ValueError:
                    print("Please give a proper input")
            if a[x-1][y-1]==".":
                if(validornot(x-1,y-1,1,0)):
                    break
            else:
                print("You are not allowed to rewrite the previous moves")
            print("Not a legal move!!!")
        swap(x-1,y-1,1,0)
    else:
        print("Player 1, you have no legal moves so your opponent will be playing until you get one.")
        p1=1
    print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
    for i in range(8):
        print("["+str(i+1)+"]", end="  ")
        for j in range(8):
            print(a[i][j], end="   ")
        print("\n")
    counter=count()
    print("Player 1: "+str(counter[1])+"  CPU: "+str(counter[0]))
    if(counter[0]==0):
        print("Player 1 wins!!!")
    elif(counter[1]==0):
        print("CPU wins!!!")
    if(counter[0]+counter[1]==64):
        if counter[0]>counter[1]:
            print("CPU wins!!!")
            break
        elif counter[1]>counter[0]:
            print("Player 1 wins!!!")
            break
        else:
            print("It's a draw")
            break

    b=[]
    if(checkforlegalmoves(0,1)):
        b=comp(0,1)
        x,y=b[0],b[1]
        print("CPU's turn(0): "+str(x+1)+" "+str(y+1))
        swap(x,y,0,1)    
    else:
        print("CPU has got no legal moves so you can play until CPU gets one.")
        p2=1
    print("    [1] [2] [3] [4] [5] [6] [7] [8]\n")
    for i in range(8):
        print("["+str(i+1)+"]", end="  ")
        for j in range(8):
            print(a[i][j], end="   ")
        print("\n")
    counter=count()
    print("Player 1: "+str(counter[1])+"  CPU: "+str(counter[0]))
    if(counter[0]==0):
        print("Player 1 wins!!!")
    elif(counter[1]==0):
        print("CPU wins!!!")
    if(counter[0]+counter[1]==64):
        if counter[0]>counter[1]:
            print("CPU wins!!!")
            break
        elif counter[1]>counter[0]:
            print("Player 1 wins!!!")
            break
        else:
            print("It's a draw")
            break
    if(p1==1 and p2 ==1):
        if counter[0]>counter[1]:
            print("CPU wins!!!")
            break
        elif counter[1]>counter[0]:
            print("Player 1 wins!!!")
            break
        else:
            print("It's a draw")
            break