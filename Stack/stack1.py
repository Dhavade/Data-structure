# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:00:43 2021

@author: Admin
"""

'''stak problem
stak is data stucture
stack is last in first out//first in last out'''

s=[]

def isempty(stk):
    if (stk==[]):
        return True
    return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1
       
def s_pop(stk):
    if (isempty(stk)):
        return('underflow')
    else:
        i=stk.pop()
        if (len(stk)==0):
            top=None
        else:
            top=top-1
    return i

def peek(stk):
    if (isempty(stk)):
        return ("underflow")
    else:
        top=len(stk)-1
        return stk[top]
    
def display(stk):
     if (isempty(stk)):
         print("stk is empty")
     else:
         top=len(stk)-1
         print(stk[top],'<-----')
         for i in range(top-1,-1,-1):
             print(stk[i])
             
while True:
    print('stak implimenstation')
    print('1. push')
    print('2. pop')
    print('3. peek')
    print('4. display')
    print('5. exit')
    
    ch=int(input("enter tha choice (1-5): "))
    if (ch==1):
        item=int(input('enter tha item you whant to push: '))
        push(s,item)
        print(f"{item} added successfully")
        input('press any key to countinue')
    elif (ch==2):
        item=s_pop(s)
        if (item=='underflow'):
            print("stack is empty")
        else:
            print(f"{item} is popped")
        input('press any key to countinue')    
    elif (ch==3):
        item=peek(s)
        if (item=='underflow'):
            print("stack is empty")
        else:
            print(f"{item} is at tha top")
        input('press any key to countinue') 
    elif (ch==4):
        display(s)
        print('press any key and countinue')
    elif (ch==5):
        break
    else:
        print('Andhe 1-5 chalana tha')
        input("press ant key to countinue")
        










             
             
    
    
    
            


