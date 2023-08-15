class Students:
    # methods
    def greet(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your gender is {self.gender} ")

    def getdata(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g


s1 = Students()

s1.getdata("snehal", 24, "female")
s1.greet()
print("--------")
