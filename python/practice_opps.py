# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius


# #     def area(self):
# #         return (22/7)*self.radius ** 2 #area of circle=pi*r**
    
# #     def perimeter(self):
# #         return 2* (22/7)*self.radius 


# # c1 =Circle(21)
# # print(c1.area())
# # print(c1.perimeter())



# class Employee:
#     def __init__(self, name,role, dept, salary):
#         self.name=name
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetailes(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.dept}")
#         print(f"Salary: {self.salary}")



# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Elon musk","Engineer", "IT", 50000)

# engg1=Engineer("Elonmusk",40)
# engg1.showDetailes()




class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price


odr1 = order("Chips",20)
odr2 =order("tea",15)

print(odr1 > odr2)  #True
