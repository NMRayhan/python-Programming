
mark1, mark2, mark3, mark4 = int(input("Enter Mark1 : ")), int(input("Enter Mark2 : ")), int(input("Enter Mark3 : ")), int(input("Enter Mark4 : "))
'''if(mark1>=80):
    print("You Have A+ Grade \n")
elif(mark1>=70):
    print("You Have A Grade \n")
elif(mark1>=65):
    print("You Have A- Grade \n")
elif(mark1>=60):
    print("You Have B Grade \n")
elif(mark1>=50):
    print("You Have C Grade \n")
elif(mark1>=40):
    print("You Have D Grade \n")
else:
    print("Fail\n")'''
'''if(mark1==40):
    print("Pass ")
if(mark1>=40):
    print("Pass")
if(mark1<40):
    print("Fail")
if(mark1>=50):
    print("Pass >= 50")'''
'''if(mark1>mark2):
    print("Mark1 is Highest")
elif(mark2>mark1):
    print("Mark2 is Highest")
elif(mark1==mark2):
    print("Mark 1 and Mark2 is Same Value ")
else:
    print("Nothing to else ")'''
if(mark1>mark2):
    if(mark1>mark3):
        if(mark1>mark4):
            print(f"{mark1} is Highest mark ")
        else:
            print(f"{mark4} is Highest Mark ")
    else:
        print(f"{mark3} is Highest Mark")
elif(mark2>mark3):
    if(mark2>mark4):
        if(mark2>mark1):
            print(f"{mark2} is Highest Mark ")
        else:
            print(f"{mark1} is Highest Mark ")
    else:
        print(f"{mark4} is Highest Mark ")
elif(mark3>mark1):
    if(mark3>mark2):
        if(mark3>mark4):
            print(f"{mark3} is Highest Mark ")
        else:
            print(f"{mark4} is Highest Mark ")
    else:
        print(f"{mark2} is Highest Mark ")
elif(mark4>mark1):
    if(mark4>mark2):
        if(mark4>mark3):
            print(f"{mark4} is Highest Mark ")
        else:
            print(f"{mark3} is Highest Mark ")
    else:
        print(f"{mark2} is Highest Mark ")