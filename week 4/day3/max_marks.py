# find max marks in a dict

a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "phy": 80}
b = []
for i in a.values():
    b.append(i)
print(b)
print(max(b))

# shortcut
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "phy": 80}
print(max(a.values()))

# with logic not using methoda
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "phy": 80}

maxi = 0
for i in a.values():
    if i > maxi:
        maxi = i
print(maxi)


# print max marks with subject name
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "maths": 80}

maxi = 0
sub = ""
for k, v in a.items():
    if v > maxi:
        maxi = v
        sub = k
print(f"the maxi marks is {maxi} of {sub}")

# using true
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "maths": 80}

maxi = 0
sub = True
for k, v in a.items():
    if v > maxi:
        maxi = v
        sub = k
print(f"the maxi marks is {maxi} of {sub}")
