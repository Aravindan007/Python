a=['7','75','76','10','415']
a.sort(reverse=True)
b=a[1]
c=a[0]
if(a[0]>a[1]):
    a[0]=b
    a[1]=c
print(a)

