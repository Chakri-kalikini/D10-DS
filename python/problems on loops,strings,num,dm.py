##sum of n natural num
# n = int(input("Enter a num: "))

# i =1
# sum=0
# while i <= n:
#     sum = sum + i
#     i+=1
#     print(sum)
    
   


    


# n = int(input("Enter a num: "))    

# for i in range(1,n+1):
#     print(i)


##print even num from 1 to N

# n =int(input("Enter a num: "))
# i =1
# while i<=n:
#     if i%2==1:
#         print(i)

#     i+=1


##multiplication of a num

# 
# n = int(input("Enter a num: "))

# for i in range(1,11): 
#     print(n,"x",i,"=",n*i)

##factoriial

n = int(input("Enter a num: "))

factorial =1

while n>0:
    factorial = factorial * n
    n-=1
    print("Factorial of",n,"is",factorial)
