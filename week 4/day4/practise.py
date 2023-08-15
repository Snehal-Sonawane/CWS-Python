# sort a dict by keys
a = {11: 23, 5: 45, 2: 12, 6: 66}
b = []
c = {}
for i in a.keys():
    b.append(i)
b.sort()
print(b)
for k in b:
    c.update({k: a.get(k)})
print(c)

# 2nd method
a = {11: 23, 5: 45, 2: 12, 6: 66}
c = {}
b = sorted(list(a.keys()))
for k in b:
    c.update({k: a.get(k)})
print(c)

# 3rd method
a = {11: 23, 5: 45, 2: 12, 6: 66}
c = {}
for k in sorted(list(a.keys())):
    c.update({k: a.get(k)})
print(c)
