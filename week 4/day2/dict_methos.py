# clear
a = {"name": "snehal", "age": 24, "gender": "female"}
print(a)
a.clear()  # to clear dict
print(a)

# copy
a = {"name": "snehal", "age": 24, "gender": "female"}
b = a
a.copy()
print(b)

# get

a = {"name": "snehal", "age": 24, "gender": "female"}
r = a.get("name")  # get method gives a value of key
print(r)

# if key is exist or not
a = {"name": "snehal", "age": 24, "gender": "female"}
if a.get("name") != None:
    print(a["name"])
else:
    print("key does not exits")


# to ask user key name if key is exist or not
a = {"name": "snehal", "age": 24, "gender": "female"}
keyname = input("Enter keyname = ")
if a.get(keyname) != None:
    print(a[keyname])
else:
    print("key does not exits")


# keys
a = {"name": "snehal", "age": 24, "gender": "female"}
r = a.keys()
print(r)

for i in r:
    print(i)  # only gives key

# 2nd method
for i in a.keys():
    print(a[i])  # only gives values of key

for i in a.keys():
    print(i, a[i])  # gives values and key both

# values
a = {"name": "snehal", "age": 24, "gender": "female"}
for i in a.values():  # gives only values
    print(i)

# sum of all values
a = {"com": 89, "his": 24, "sci": 80}
sum = 0
for i in a.values():
    sum = sum + i
print(sum)

# make a dict and sum of all values of key
a = {}
for i in range(0, 3):
    sub = input("Enter sub= ")
    marks = int(input("Enter marks= "))
    a[sub] = marks
print(a)
sum = 0
for i in a.values():
    sum = sum + i
print(sum)

# print
# marks in com is 44
# marks in sci is 89
# marks in geo is 80

a = {"maths": 34, "sci": 68, "com": 78}
for i in a.keys():
    print(f"marks in {i} is {a[i]}")

# 2nd method using "items" method
a = {"maths": 34, "sci": 68, "com": 78}

for k, v in a.items():
    print(f"marks in {k} is {v}")
