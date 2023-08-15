a = [3, 4, 2, 56, 33, 87, 11]
even = 0
odd = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("even number = ", even)
print("odd number = ", odd)

# 2nd method
a = [3, 4, 2, 56, 33, 87, 11]
even = []
odd = []
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(f"number of even value = {len(even)}")
print(f"number of odd value = {len(odd)}")
