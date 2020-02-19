#leap Year
"""

year = int(input("Enter Year Number : "))

if year%400==0:
    Result = "Leap Year"
elif year%4==0 and year%100!=0:
    Result = "Leap Year"
else:
    Result = "Not Leap Year"
print(Result)

print(bool(""))#empty String
print(bool(0))#0 Return False
print(bool(False))#Return False
print(bool({}))#Return False
print(bool([]))#Return False
print(bool(()))#Return False
"""

'''Latter = input("Enter Latter \n")
if Latter == "a" or Latter == "e" or Latter == "i" or Latter == "o" or Latter == "u":
    print("this is Vowel")
else:
    print("Consonant") '''
OrginalWord = input("Enter A Word ")
Word = OrginalWord.lower()

first = Word[0]

if first in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
