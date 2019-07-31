n=int(input("Enter"))
l=[]
for i in range(0,n):
    a=input("")
    l.append(a)
l1=[]
for i in range(0,len(l)):
    a=l[i]
    a=a[1:len(a)-1]
    l1.append(a.split(','))
maxs=0
l2=[]
for i in range(0,len(l1)):
    b=l1[i]
    if(b[2]=='entry'):
        maxs=maxs+int(b[1])
        l2.append(maxs)
    elif(b[2]=='exit'):
        maxs=maxs-int(b[1])
        l2.append(maxs)
z=max(l2)
c=l2.index(z)
q=l1(c)
print(q[0],end=' ')
for i in range(c,len(l2)):
    if l2[i]<z:
        c1=l2.index(l2[i])
        q1=l2[c1]
        break
print(q1[0])



    
