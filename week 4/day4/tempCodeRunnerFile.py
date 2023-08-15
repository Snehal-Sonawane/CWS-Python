a={11:23,5:45,2:12,6:66}
c={} 
for k in sorted(list(a.keys())):
    c.update({k:a.get(k)})
print(c) 