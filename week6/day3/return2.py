def abc(a: list):
    t = sum(a)
    return t


def check(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


x = abc([10, 20, 30])
print(x)
check(x)
