class Circle:
    def __init__(self,r,r1):
        self.radius=r
        self.radius1=r1
    def area(self):
        self.a=self.radius*2
        print(self.a)
        
    def perimeter(self):
        self.p=self.radius1*2*3.14
        print(self.p)
s=Circle(2,3)
s1=Circle(4,6)
#s.display()
s.area()
s1.perimeter()

        
