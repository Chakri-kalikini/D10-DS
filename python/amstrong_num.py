num=int(input("Enter the number: "))
length =len(str(num))

temp=num
sum=0
while temp>0:
    digit =temp%10
    sum+=digit ** length
    temp=temp//10
print("Number is {} and sum is {}".format(num , sum))
if sum==num:
    print("The number is Amstrong number")
else:
    print("Not an Amstrong number")

# #adding the numbers with tthe no of power it has withs no of digits with that the given number should be eqal to the sum of the powe of the given number.
# num=int(input("Enter the number: "))
# length=len(str(num))

# temp=num
# sum=0
# while temp>0:
#     id=temp%10
#     sum+=id**length
#     temp=temp//10
#     print("number is {} and sum is{}".format(num ,  sum))
#     if sum==num:
#         print("The number is Amstrong number")
#     else:
#         print("Not an Amstrong number")


##palendrome
# num=int(input("Enter the num: "))
# temp=num
# rev=0
# while temp>0:
#     id=temp%10
#     rev=rev*10+id
#     temp=temp//10
#     print(rev)
#     if rev==num:
#         print("the number is an palindrome")
#     else:
#         print("not an palindrome")

#fizz buzz
# num=int(input("Enter the number: "))
# if num%3==0 and num%5==0:
#     print(f"{num}-fizz buzz")
# elif num%3==0:
#     print(f"{num}-fizz")
# elif num%5==0:
#     print(f"{num}-buzz")
# else:
#     print("not divisable by 5 and 3")

##from 1 -30 add even numbers and multiply odd numbers using for loop
# sum=0
# product=1
# for i in range(1,31):
#     if i%2==0:
#         sum+=i
#     else:
#         product*=i
# print(f"sum of even numbes is {sum} and product of odd numbers is {product}")

##print vowels from "something"
# str1="something"
# x=0
# while x<len(str1):
#     if str1[x] in "aeiou":
#         print(str1[x])
#     x+=1

# str1="something"
# x=len(str1)-1
# while x<0:
#     if str1[x] in "aeiou":
#         print(str1[x])
#     x+=1

##print only alphabet e from "something"
# str1="something"
# x=0
# while x<len(str1):
#     if str1[x] in "e":
#         print(str1[x])
#     x+=1


              