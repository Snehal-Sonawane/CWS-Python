def marks(phy, chem, com, sci):  # parameter
    print(phy + chem + com + sci)


marks(56, 67, 89, 90)  # agruments


def greet(name):
    print(f"greeting is {name}")


greet("snehal")


def add(a, b, c):
    print(a + b + c)


add(12, 23, 45)


def marks(phy, sci, eng, com):
    total = phy + sci + com + eng
    c = (total / 400) * 100
    print(c)


marks(45, 56, 79, 89)
