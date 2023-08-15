a = [23, 45, 60, 98, 77]
num = int(input("Enter an integer: "))

if num in a:
    print("yes")
else:
    print("no")

# count a number by user
a = [34, 56, 34, 70, 34, 80, 56]
n = int(input("Enter an integer: "))

if a.count(n) >= 1:
    print("yes")
else:
    print("no")

# 2nd method
if num not in a:
    print("not exists")
else:
    print("exists")
