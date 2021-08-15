# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:46:25 2021

@author: Admin
"""
"queue is fiest n fiest out and last in last out"
queue=[]
def enqueue():
    element=input("enter tha element")
    queue.append(element)
    print(element,"is added to queue")
    
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("remove element:",e)
        
def display():
    print(queue)

while True:
    print("enter tha operations 1.added 2.remove 3.show 4.quit")
    choice=int(input()) 
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter tha correct choice")
        
    
    