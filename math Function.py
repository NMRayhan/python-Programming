import math

n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))

print(f" {n1} + {n2} = {n1+n2}")
print(math.factorial(3))
print(math.ceil(3.4))
print(math.floor(3.4))
print(math.gcd(12,12))
print("For Area \n")
Base = float(input("Enter Base : "))
height = float(input("Enter Height : "))

area = .5*Base*height
a = int(area) #type kasting
print(a)

print("For Circle \n")
Radius = int(input("Enter Radius : "))
circle = math.pi * (Radius**2)
print("Area of This Circle : ",circle)