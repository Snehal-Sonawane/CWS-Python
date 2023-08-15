prime = int(input("Enter number = "))
count = 0
for i in range(1, prime + 1):
    if prime % i == 0:
        count = count + 1
        print(i, end=" ")
print()
print(count)
if count == 2:
    print("it is prime number")
else:
    print("it is composite number")

num = int(input("Enter number = "))
c = 0
for i in range(1, num + 1):
    if num % i == 0:
        c = c + 1
        print(i, end=" ")
print()
print(c)
if c == 2:
    print(c)
