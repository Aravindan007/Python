a=int(input("Enter"))
def fib(a):
    if (a<0):
            print("not correct")
    elif(a==0):
            return 0
    elif (a==1):
              return 1
    else:
          return fib(a-1)+fib(a-2)
print (fib(a))
