a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
maxi = a[0]
for i in range(1, len(a)):
    if a[i] > maxi:
        maxi = a[i]
print(maxi)

a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
mini = a[0]
for i in range(1, len(a)):
    if a[i] < mini:
        mini = a[i]
print(mini)
