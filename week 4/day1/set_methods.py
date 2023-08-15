set1 = {12, 34, 55, 67, 88, 20}
set = {12, 67, 100, 200}


# union/intersection
set1 = {12, 34, 55, 67, 88, 20}  # mix a set remove duplicate
set2 = {12, 67, 100, 200}
result = set1.union(set2)
print(result)


set1 = {12, 34, 55, 67, 88, 20}
set2 = {12, 67, 100, 200}
r = set1.intersection(set2)  # only common elements are print
print(r)

# add element
set1 = {12, 34, 55, 67, 88, 20}
print(set1)
set1.add(100)
print(set1)

# remove element
set1 = {12, 34, 55, 67, 88, 20}
print(set1)
set1.remove(12)
print(set1)
