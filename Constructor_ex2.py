"""Create account class with 2 attributes - balance & account no. 
    Create methods for debit, credit & printing the balance."""

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total balance :", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance :", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)

#OR

#y = int(input("Enter account number:"))
#x = int(input("Enter amount you want to debit:"))
#acc2 = Account(100000,y)
#acc2.debit(x)