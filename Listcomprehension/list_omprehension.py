import datetime
import time

t1 = datetime.datetime.now()
print(t1)
time.sleep(2)
t2 = datetime.datetime.now()
print(t2)
print(t2 - t1)


import datetime
import time

a = []
t1 = datetime.datetime.now()
for i in range(1, 50000001):
    a.append(i)
t2 = datetime.datetime.now()

print(t2 - t1)


import datetime
import time

t1 = datetime.datetime.now()
a = [i for i in range(1, 50000001)]
t2 = datetime.datetime.now()
print(t2 - t1)
