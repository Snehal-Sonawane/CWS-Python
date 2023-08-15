a = [3, 4, 2, 56, 33, 87, 11]
even = []
odd = []
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        odd.append(a[i])
print(odd) 