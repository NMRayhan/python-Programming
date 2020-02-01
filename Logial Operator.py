#leap Year
year = int(input("Enter Year Number : "))

if year%400==0:
    Result = "Leap Year"
elif year%4==0 and year%100!=0:
    Result = "Leap Year"
else:
    Result = "Not Leap Year"
print(Result)