# class Student:  
#     def __init__(self, name):  # Fixed the typo here
#         self.name = name  

# s1 = Student("Shradha")  # Now this works
# print(s1.name)  # Output: Shradha  

# del s1.name  # Deletes the 'name' attribut)
# 
# 
# 
# 
# 
class Account: #class
    def __init__(self, acc_no, acc_pass):#constructor
        self.acc_no=acc_no
        self.__acc_pass=acc_pass





acc1 =Account("12345", "abcde")#obj

print(acc1.acc_no)
print(acc1.acc__pass)
