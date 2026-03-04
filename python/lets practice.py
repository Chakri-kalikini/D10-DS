class account:  #class
    def __init__(self,bal,acc): #constructor
        self.balance=bal
        self.account_no=acc

    #debit method

    def debit(self, amount):
        self.balance-=amount
        print("Rs.",amount, "was debiteed")
        print("total balance=", self.get_balance())

    def credit(self, amount):
        self.balance+=amount
        print("Rs.",amount, "was credited")
        print("total balance=", self.get_balance())

    def get_balance(self):
        return self.balance
    




acc1=account(10000,12345) #object creation
acc1.debit(99999)
acc1.credit(100000)