# print commom elements in list
a = [21, 45, 67, 80]
b = [21, 80, 44, 33]
result = list(set(a).intersection(set(b)))
print(result)
