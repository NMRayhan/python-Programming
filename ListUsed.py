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
a = 6
b = 3
print(math.floor(b/a))
print(math.ceil(b/a))
print(b//a)
print(math.comb(6,3))
fact_A = math.factorial(a)
print(fact_A)
fact_B = math.factorial(b)
print(fact_B)
result = (fact_A)/(fact_B*(fact_A-fact_B))
print(result)