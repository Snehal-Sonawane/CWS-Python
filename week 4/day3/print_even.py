# put 5 sub and marks in dict
# print total of all marks divi by 2

a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "phy": 80}
total = 0
for m in a.values():
    if m % 2 == 0:
        total = total + m
print(total)

# 2nd method
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "phy": 80}
total = 0
for m in a.keys():
    if a[m] % 2 == 0:
        total = total + a[m]
print(total)
