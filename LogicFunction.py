a = int(input("1st Line \t"))
m = int(input("1st Degree \t"))
b = int(input("2nd Line \t"))
n = int(input("2nd Degree \t"))
c = int(input("3rd Line \t"))
o = int(input("3rd Degree \t"))
d = int(input("4th Line \t"))
p = int(input("4th Degree \t"))

if(a==b==c==d):
    if(m==n==o==p):
        print("This is Square Field")
    else:
        print("This is rectangle")
else:
    print("This is not Square Field or Rectangle")
