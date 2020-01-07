class Officer:
    def __init__(self,name=None,age=0,city=None,phone=None):
        self.name=name
        self.phone=phone
        self.age=age
        self.city=city
person=[]
n=int(input("No of officers:"))
for i in range(n):
    name=input("Name: ")
    age=int(input("age: "))
    phone=int(input("Phone: "))
    city=input("City: ")
    a=Officer(name,age,phone,city)
    person.append(a)
print("Name and age")
for i in person:
    print(i.name)
    print(i.city)
print("phone number")
p=0
for i in person:
    if(i.name=="Abi"):
        p=1
        print(i.phone)
if(p==0):
    print("invalid name")
print(Officer.__name__)
print("")
print("----------------------------")
print("All officers")
for i in person:
    print(i.name)
    print      (i.age)
    print (i.city)
    print      (i.phone)
    
