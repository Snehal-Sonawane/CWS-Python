a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}
# print(a["sanjay"])
# print(a["sagar"])
# print(a["akul"])
# print(a.get("sanjay")) #2nd method
print(a["sagar"][2])


# print student along with total marks

a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}

for k, v in a.items():
    print(f"{k} has scored {sum(v)}")

#
a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}
for k, v in a.items():
    print(k)
    for i in v:
        print(i)

# revered order
a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}

for k, v in a.items():
    print(k)
    for i in v[::-1]:
        print(i)


# find max marks with keys
a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}


for k, v in a.items():
    print(f"{k} -> {max(v)}")

# 2nd method without max method
for k, v in a.items():
    max_m = 0
    for m in v:
        if m > max_m:
            max_m = m

    print(k, max_m)


# find over all max
a = {
    "sagar": [67, 74, 32, 12, 44],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}

max_m = 0
for k, v in a.items():
    for m in v:
        if m > max_m:
            max_m = m
print(max_m)

# 2nd method
a = {
    "sagar": [67, 74, 32, 12, 94],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}
result = []
for k, v in a.items():
    result.extend(v)  # extend works mix the all list in one list only value not bracket
print(max(result))


# marks with keys
a = {
    "sagar": [67, 74, 32, 12, 94],
    "sanjay": [76, 32, 120, 34, 33],
    "akul": [76, 88, 32, 4, 56],
}
result = []
for k, v in a.items():
    result.extend(v)
max_marks = max(result)
for k, v in a.items():
    if max_marks in v:
        print(k, max_marks)
