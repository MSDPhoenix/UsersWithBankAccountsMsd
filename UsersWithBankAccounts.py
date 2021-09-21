# BASIC ASSIGNMENT SUCCESSFUL

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


#SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# FIRST ATTEMPT SUCCESSFUL:

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
        self.account1 = BankAccount()
        self.account2 = BankAccount()
    def make_deposit1(self,amount):
        self.account1.deposit(amount)
        return self
    def make_withdrawal1(self,amount):
        self.account1.withdraw(amount)
        return self
    def display_user_balance1(self):
        print(self.name,"account 1 balance",self.account1.balance)
        return self
    def transfer_money1(self,other_user,amount):
        self.make_withdrawal1(amount)
        other_user.make_deposit1(amount)
        print(f"Transfering {amount} from {self.name} to {other_user.name}")
        return self
    def make_deposit2(self,amount):
        self.account2.deposit(amount)
        return self
    def make_withdrawal2(self,amount):
        self.account2.withdraw(amount)
        return self
    def display_user_balance2(self):
        print(self.name,"account 2 balance",self.account2.balance)
        return self
    def transfer_money2(self,other_user,amount):
        self.make_withdrawal2(amount)
        other_user.make_deposit2(amount)
        print(f"Transfering {amount} from {self.name} to {other_user.name}")
        return self


    
Jay = User("Jay Pritchett","jaypritchett@Pritchettsclosets.com")
Gloria = User("Gloria Pritchett","spicycolumbian@gmail.com")
Claire = User("Claire Dunphy","toomanytequilas@yahoo.com")

Jay.make_deposit2(1200).make_deposit1(1000).make_deposit1(1000).make_withdrawal1(330).display_user_balance1().display_user_balance2()

Gloria.make_deposit1(1000).make_deposit1(1000).make_withdrawal2(330).make_withdrawal1(330).display_user_balance1().display_user_balance2()

Claire.make_deposit1(1000).make_withdrawal1(330).make_withdrawal1(330).make_withdrawal1(330).display_user_balance1().display_user_balance2()

Jay.transfer_money1(Claire,500).display_user_balance1().display_user_balance2()
Claire.display_user_balance1().display_user_balance2()




#THIS IS SECOND ATTEMPT.  THIS ATTEMPT FAILED, SO I REVERTED BACK TO FIRST ATTEMPT

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
        self.account1 = BankAccount()
        self.account2 = BankAccount()
    def make_deposit(self,amount,account_num):
        self.account_num.deposit(amount)
        return self
    def make_withdrawal(self,amount,account_num):
        self.account_num.withdraw(amount)
        return self
    def display_user_balance(self,account_num):
        print(self.name,"account balance",self.account_num.balance)
        return self
    def transfer_money(self,acount_num,amount,other_user,other_num):
        self.make_withdrawal(amount,account_num)
        other_user.make_deposit(amount,other_num)
        print(f"Transfering {amount} from {self.name} to {other_user.name}")
        return self


    
Jay = User("Jay Pritchett","jaypritchett@Pritchettsclosets.com")
Gloria = User("Gloria Pritchett","spicycolumbian@gmail.com")
Claire = User("Claire Dunphy","toomanytequilas@yahoo.com")

Jay.make_deposit(1200,account1)
Jay.display_user_balance(account1)

.make_deposit(1000,account1).make_deposit(1000,account1).make_withdrawal(330,account1)

Gloria.make_deposit(1000,account1).make_deposit(1000,account1).make_withdrawal(330,account1).make_withdrawal(330,account1).display_user_balance(account1)

Claire.make_deposit(1000,account1).make_withdrawal(330,account1).make_withdrawal(330,account1).make_withdrawal(330,account1).display_user_balance(account1)

Jay.transfer_money(account1,500,Claire,account1).display_user_balance(account1)
Claire.display_user_balance(account1)