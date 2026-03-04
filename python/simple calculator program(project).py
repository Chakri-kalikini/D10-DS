num1=int(input("Give 1st num: "))
num2=int(input("Give 2nd num: "))
operation=(input("Give operator: "))

if operation=="+":
    print(f"Addition of 2 num is {num1+num2}")
elif operation=="-":
    print(f"Subtraction of 2 num is {num1-num2}")
elif operation=="*":
    print(f"Multiplication of 2 num is {num1*num2}")
elif operation=="/":
    print(f"Division of 2 num {num1/num2}")

else:
    print("Invalid operation")