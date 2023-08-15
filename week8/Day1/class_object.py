class Students:
    # Data members
    # name=""
    # age=0
    # gender=""
    # methods
    def greet(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your gender is {self.gender} ")
        # print(self.city)

    def getdata(self):
        self.name = input("Enter name = ")
        self.age = input("Enter age = ")
        self.gender = input("Enter gender = ")
        # self.city = "surat"


s1 = Students()
s2 = Students()
s3 = Students()

# s1.name='snehal'
# s1.age=24
# s1.gender="female"
# s2.name="sushma"
# s2.age=51
# s2.gender="female"
s1.getdata()
s1.greet()
print("--------")
s2.getdata()
s2.greet()
print("--------")
s3.getdata()
s3.greet()
# print(s1.name,s1.age,s1.gender)
# print(s2.name,s2.age,s2.gender)
