def sum (n):
    if(n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter a natural number: "))
print(sum(n))  # Example usage, change 5 to any natural number you want to sum up to

