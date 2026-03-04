# def add(a,b):
#     return a+b
# result=add(3,5)
# print(result)

def greet_user(name,greeting="Hello"):
    return greeting+ "," + name+"!"

greeting1=greet_user("Bob")
greeting1=greet_user("charlie","hi")
print(greeting1)  # Output: hi, charlie!
print(greet_user("Bob"))  # Output: Hello, Bob!  # Output: Hello