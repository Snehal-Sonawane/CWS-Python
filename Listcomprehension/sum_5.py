# print all number divisible by 5 from 1 to 100
a = sum([i for i in range(1, 101) if i % 5 == 0])
print(a)

# count number divisible by 5
a = len([i for i in range(1, 101) if i % 5 == 0])
print(a)
