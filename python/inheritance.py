##single inheritence
# class car:
#     @staticmethod
#     def start():
#         print("Car started.")


#     @staticmethod
#     def stop():
#         print("Car stopped.")


# class Toyotacar(car):
#     def __init__(self, name):
#         self.name = name


# car1 =Toyotacar("fortunar")       
# car2 =Toyotacar("prius")   

# print(car1.start())
    


##multi-level inheritence

# class car:  #1st class
#     @staticmethod
#     def start():
#         print("Car started.")


#     @staticmethod
#     def stop():
#         print("Car stopped.")


# class Toyotacar(car):       #2nd class
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyotacar):   #3rd class
#     def __init__(self, type):
#         self.type=type

# car1=Fortuner("disele")
# car1.start()


##multiple inheriteance

# class A:
#     varA ="welcome to class A"

# class B:
#     varB ="welcome to class B"


# class C(A,B):
#     varC="welcome to class C"


# c1 =C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



##class method

##property method

class Student:
    def __init__(self, phy,che,math):
        self.phy = phy  
        self.che = che
        self.math = math
       

    
    @property
    def percentage(self):
        return str((self.phy +self.che+self.math)/3)+ "%"
         


stu1 = Student(90,80,70)


stu1.phy =90
print(stu1.percentage)  #percentage will not change because it is a property method
