
##Encapsulation,Abstraction:

class car:  #class
    def __init__(self): ##constructor
        self.acc =False
        self.brk =False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc =True
        print("car started..")
        

car1 =car()  ##obj
car1.start()





