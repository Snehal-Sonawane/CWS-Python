class Parent:
    def __init__(self):
        self.fathername = input("Enter father name = ")
        self.mothername = input("Enter mother name = ")


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.childname = input("Enter child name = ")

    def displayallinfo(self):
        print(f"father name = {self.fathername}")
        print(f"mother name = {self.mothername}")
        print(f"child name = {self.childname}")


o = Child()
