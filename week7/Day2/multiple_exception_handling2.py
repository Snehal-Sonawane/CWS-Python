try:
    a = [23, 45, 67, 32, 56, 78, 0]
    print(a[4])
    print(a[0] / a[-1])
except ZeroDivisionError:
    print("cannot divided by zero")
except IndexError:
    print("Wrong index given")
except:
    print("some error occured")

try:
    a = int(input("Enter number 1 = "))
    b = int(input("Enter number 2 = "))
    c = int(input("Enter number 3 = "))
    print(a + b + c)
except ValueError:
    print("plz enter proper int")
