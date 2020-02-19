sum = 0.0 #initiialize
initial = 0
while initial < 10:
    number = int(input(f"Enter Number {initial} = "))
    sum = sum + number
    initial=initial+1 #increment and end of the while loop
print(f"Total Average is {sum/initial} and Total is {sum}")
print("End of Program")