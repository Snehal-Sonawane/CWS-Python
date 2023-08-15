# lambda function
# add of 2 number
# return add of 5 number
# return sum of 5 number


x = lambda n1, n2: n1 + n2

addition = lambda n1, n2, n3, n4, n5: n1 + n2 + n3 + n4 + n5
sumOfList = lambda lst: sum(lst)

ans = x(10, 20)
print(ans)

print(addition(43, 12, 43, 54, 667))
print(sumOfList([1, 2, 3, 4, 5, 6]))
