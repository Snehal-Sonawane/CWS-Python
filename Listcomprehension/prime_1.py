n = int(input("Enter a number = "))
a = [i for i in range(1, n + 1) if n % i == 0]
print("prime" if len(a) == 2 else "not prime")

# in one line
n = int(input("Enter a number = "))
print("prime" if len([i for i in range(1, n + 1) if n % i == 0]) == 2 else "not prime")


# n=3
# print("even" if n%2==0 else"odd")
