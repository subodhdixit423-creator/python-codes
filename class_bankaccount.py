def_init_(self,account_number,initial_balance=0)
self.account_number=account_number
self.balance=initial_balance

def deposit(self,amount):
    if amount>0:
        self.balance+=amount
        print(f"₹{amount}deposited successfully.")
    else:
        print("deposit amount must be positive.")

        def withdraw(self,amount):
            if amount>0:
                if amount<=self.balance:
                    self.balance-=amount
                    print(f"₹{amount}withdrawn successfully.")
                else:
                    print("insufficient balance.")
                else:
print("withdrawal amount must be positive.")
def check_balance(self):
    print(f"current balance:₹{self.balance}")



    #example usage
    account=bank account(101,5000)

    account.check_balance()
    account.deposit(2000)
    account.withdraw(1500)
    account.check-balance()
    
