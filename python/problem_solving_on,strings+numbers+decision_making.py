
# str =input(str("No of vowels: "))
# str2 =str.lower()
# a =str2.count('a')
# e =str2.count('e')
# i =str2.count('i')
# o =str2.count('o')
# u =str2.count('u')
# print(f"Num of vowels:{a+e+i+o+u}")

##Grade calculator:

# m = int(input("Marks in maths: "))
# s = int(input("Marks in science: "))
# e = int(input("Marks in english: "))

# total_marks= m+s+e
# average=total_marks/3

# percentage =(total_marks/300)*100

# if percentage > 90:
#      print("Grade: A")

# elif percentage > 80:
#      print("Grade: B")

# elif percentage > 70:
#      print("Grade: C")

# elif percentage >30:
#      print("Grade: F")

# else:
#     print("You have failed"" "+"Better luck next time") 

# print(f"Your Avarage is {average} and \b Percentage is {percentage}")   



##palindrome checker:

# s = input("Enter a string: ")

# reverse = s[::-1]

# if reverse ==s:
#     print("This is a palindrome")

# else:
#     print("This is not a palindrome")


##largest of three numbers:

# num1 = int(input("Enter First num: "))
# num2 = int(input("Enter Second num: "))
# num3 = int(input("Enter Third num: "))

# if num1 > num2 and num1 > num3:
#     print(f"Largest number is: {num1}")

# elif num2 > num1 and num2 > num3:
#     print(f"Largest number is: {num2}")

# elif num3 > num1 and num3> num2:
#     print(f"Largest number is: {num3}")

# else:
#     print("All numbers are equal")


## leap year checker:

year =int(input("Enter a year: "))

leap = False

if year%100 == 0 and year%400 == 0:
    leap =True

elif year%4 == 0:
    leap = True
else:
    leap = False

if leap == True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

print(leap)

