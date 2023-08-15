import area

area.square(5)

x = area.rectanglr(12, 34)  # area of recangle in function
print(x)

# 2nd method
from area import square, rectanglr

square(5)
x = rectanglr(11, 22)
print(x)

# 3rd method
from area import *  # *means all function call

square(5)
x = rectanglr(11, 23)
print(x)
circle(10)
