# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:33:45 2021

@author: Admin
"""

stack=[]
def push():
    if len(stack)==n:
        print("stack is full")
    else:    
        element=input("enter tha element")
        stack.append(element)
        print(stack)
    
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("remove element",e)
        print(stack)
        
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
n=int(input("limit of stack"))            
while True:
    print('select tha oparation 1. push 2.pop 3.display 4.quit')
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter tha correct oparation")           