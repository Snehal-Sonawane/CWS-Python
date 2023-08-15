class Students:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = input("Enter age = ")
        self.gender = input("Enter gender = ")

    def greet(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your gender is {self.gender} ")


s1 = Students()
# s1 = Students()
s1.greet()
# s1.greet()


# constuctor


class Students:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

    def greet(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your gender is {self.gender} ")


s1 = Students("snehal", 24, "f")
s1.greet()
