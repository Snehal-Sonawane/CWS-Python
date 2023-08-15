class Parent:
    def setparentinfo(self):
        self.fathername = input("Enter father name = ")

    def displayparent(self):
        print("display of parent class is being called")
        print(self.fathername)


class Child(Parent):
    def setchildinfo(self):
        self.childname = input("Enter child name = ")

    def displaychild(self):
        print("display of child class is being called")
        print(self.childname)

    def displayallinfo(self):
        print(f"father name = {self.fathername}")
        print(f"child name = {self.childname}")


o = Child()
o.setparentinfo()
o.setchildinfo()
o.displayallinfo()
