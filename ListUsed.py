import math
Number = [1,2,3,4,5,6,7,8,9,10]
print(Number)
print(Number[0])
print(Number[5])
print(Number[10-4])
print("Total Number is This List ",len(Number))

print(3 in Number)
print(10 in Number)
print(11 not in Number)
a = Number[3]
b = Number[8]
print(math.floor(b/a))
print(math.ceil(b/a))
print(b//a)