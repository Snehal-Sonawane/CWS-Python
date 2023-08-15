a = "aeroplane is good transport"
b = a.split()
print(b)
b.reverse()
print(b)
print(" ".join(i for i in b))

user_string = "aeroplane is a good mode of transport good bye ok done"
b = user_string.split()
print(b)
for i in b[::2]:
    print(i, end=" ")

# 2nd method
user_string = "aeroplane is a good mode of transport good bye ok done"
b = user_string.split()[::2]
print(b)
print(" ".join(i for i in b))

# 3rd method
user_string = "aeroplane is a good mode of transport good bye ok done"

print(" ".join(i for i in user_string.split()[::2]))

user_string = "aeroplane ok is a good mode of a transport good bye ok done"
b = user_string.split()
print(b)
r = set(user_string)
print(r)
s = list(r)
print(s)

user_string = "aeroplane ok is a good mode of a transport good bye ok done"
b = user_string.split()
print(b)
for i in b:
    print(i[::-1], end=" ")


user_string = "aeroplane ok is a good mode of a transport good bye ok done"
b = user_string.split()
print(b)
for i in b:
    print(i[::-1], end=" ")
