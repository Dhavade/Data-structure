#a=input()
b=[]
s=[]
d=[]
b=[]
for i in range(6):
    b.append(input("enter number"))
print(b) 
for i in b:
    if (i<0):
        s.append(i)
    elif (i>0):
        d.append(i)
    else:
        b.append(i)
print(len(s)%6)    
print(len(b)%6)    
print(len(d)%6)    


