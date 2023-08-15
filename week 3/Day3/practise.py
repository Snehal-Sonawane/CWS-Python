# sepearte all even and odd number in list
a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# how many times elements are repeted
a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
for i in b:
    count = a.count(i)
    print(f"{i} occurs {count} times")

# Q5. Write a python program which prints all the values whose
# count is greater than 3. (Make sure to make a list with at least 15
# numbers)

a = [23, 34, 12, 23, 77, 34, 12, 77, 23, 77, 45, 35, 77, 23, 10, 12, 8, 12]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
for i in b:
    count = a.count(i)
    if a.count(i) >= 3:
        print(f"{i} occurs {count} times")
