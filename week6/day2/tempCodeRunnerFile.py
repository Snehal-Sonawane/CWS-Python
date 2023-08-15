class Rectangle:
    def inputDimension(self):
        self.length=int(input("Enter a length  = "))
        self.width=int(input("Enter a width  = "))

    def area(self):
        print(f"Area is {self.width*self.length}")

s1=Rectangle()
s1.inputDimension()    
s1.area()
