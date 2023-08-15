class Abc:
    def setchild(self, childobj):
        self.child = childobj

    def display(self):
        self.child.displaychild()


class Xyz:
    def displaychild(self):
        print("I am display")


obj = Xyz()
obj1 = Abc()
obj1.setchild(obj)
obj1.display()
