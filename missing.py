a=int(input(""))
l=[]
for i in range(0,a):
    b=int(input(""))
    l.append(b)
x=l[0]
for i in range(l[0],l[-1]):
    if x not in l:
        print(x)
    x=x+1
    
        
