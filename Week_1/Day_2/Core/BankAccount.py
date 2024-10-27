class BankAcount:
    def __init__(self, interestRate, balance):
        self.interestRate=interestRate
        self.balance=balance

    def Deposit (self, amount):
        self.balance = self.balance + amount
        return self
        

    def Withdraw (self,amount):
        if (self.balance-amount) > 0 :
            self.balance -= amount
        else:
            print ( "Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        

    def display_acount_info (self):
        print(f"Balance: {self.balance}$")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.interestRate)


mounir_user = BankAcount(0.05,100)
mounir_user.Deposit(300).Deposit(100).Deposit(80)
mounir_user.Withdraw(150)
mounir_user.display_acount_info()
mounir_user.yield_interest()
mounir_user.display_acount_info()

mounir_user1 = BankAcount(0.06,100)
mounir_user1.Withdraw(120)
mounir_user1.display_acount_info()
mounir_user1.yield_interest()
mounir_user1.display_acount_info()






