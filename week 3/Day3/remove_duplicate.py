# remove duplicate in a put in b list
a = [34, 56, 34, 70, 34, 80, 56]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

# count the number of frequncy of each number
for i in b:
    count = a.count(i)
    print(f"{i} occurs{count} times")


# count a number by user
a = [34, 56, 34, 70, 34, 80, 56]
n = int(input("Enter an integer: "))

if a.count(n) >= 1:
    print("yes")
else:
    print("no")
