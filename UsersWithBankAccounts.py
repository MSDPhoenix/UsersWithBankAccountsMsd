class BankAccount:
    def __init__(self,int_rate=.01,balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance <amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: ",self.balance)
        return self
    def yield_interest(self):
        if self.balance >0:
            self.balance = self.balance*(1+self.int_rate)
        return self
    
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount()
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.name,"account balance",self.account.balance)
        return self
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"Transfering {amount} from {self.name} to {other_user.name}")
        return self
        
    
Jay = User("Jay Pritchett","jaypritchett@Pritchettsclosets.com")
Gloria = User("Gloria Pritchett","spicycolumbian@gmail.com")
Claire = User("Claire Dunphy","toomanytequilas@yahoo.com")

Jay.make_deposit(1200).make_deposit(1000).make_deposit(1000).make_withdrawal(330).display_user_balance()

Gloria.make_deposit(1000).make_deposit(1000).make_withdrawal(330).make_withdrawal(330).display_user_balance()

Claire.make_deposit(1000).make_withdrawal(330).make_withdrawal(330).make_withdrawal(330).display_user_balance()

Jay.transfer_money(Claire,500).display_user_balance()
Claire.display_user_balance()