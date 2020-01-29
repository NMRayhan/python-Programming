import math
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