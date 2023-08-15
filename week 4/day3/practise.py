# copy a dict put in b and add 5 in all values in dict
a = {"com": 89, "geo": 90, "his": 67, "sci": 78, "maths": 80}
b = {}
for k, v in a.items():
    b[k] = v + 5

print(b)

# b={'com': 'pass', 'geo': 'fail', 'his': 'pass', 'sci': 'fail', 'maths': 'pass'}
a = {"com": 89, "geo": 20, "his": 39, "sci": 11, "maths": 80}
b = {}
for k, v in a.items():
    if v >= 40:
        b[k] = "pass"
    else:
        b[k] = "fail"
print(b)
