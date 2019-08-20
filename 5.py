logs=int(input("Enter the logs"))
lists=[]
a1=[]
a2=[]
a3=[]
a4=[]
minute=0
for i in range(0,logs):
    a=input("Enter the log")
    lists.append(a)
for i in lists:
    a=i
    b=i
    a=a[2:11]
    b=b[12:23]
    x=a.split(':')
    y=b.split('-')
    a1.append(x)
    a2.apend(y)
for i in a1:
    minutes=(3600*a[0])
    minutes=(12*a[1])
    a3.append(minutes)
    
        
    
    


