# exception handling

try:
    a = int(input("Enter a number = "))
    b = int(input("Enter a number = "))
    print(a / b)
except:
    print("some error occured")
else:
    print("this is else statement")  # this optional  #if error else statement not print

finally:
    print(
        "this is final statement")  # this optional  # finally if error or not bt finally print
