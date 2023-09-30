 '''
Define a class to represent a bank account. Include the following members:

    Data members

      (a) Name of the depositor
      (b) Account number
      (c) Type of account
      (d) Balance amount in the account

    Member functions

      (a) To assign initial values
      (b) To deposit an amount
      (c) To withdraw an amount after checking the balance
      (d) To display name and balance

  Write a main program to test the program.
'''

class BankAccount:
    def __init__(self,name,account_number,type_of_account):
        self.name=name
        self.account_number=account_number
        self.type_of_account=type_of_account
        self.balance=0.0
        
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f'Deposited amount = {amount}\nNew balance = {self.balance}')
        else:
            print(f'Invalid deposit amount. Please enter valid amount')
            
    def withdraw(self,amount):
        if amount>0:
            if amount <=self.balance:
                self.balance -=amount
                print(f'Withdrew amount = {amount}\nNew balance = {self.balance}')
            else:
                print('Insufficient amount')
        else:
            print('Invalid withdrew amount')
            
    def display(self):
        print(f'Account holder {self.name}')
        print(f'Account number {self.account_number}')
        print(f'Account type {self.type_of_account}')
        print(f'Account balance {self.balance}')
              
#create a bank account1
account1=BankAccount('Adeeba',620214567,'saving')

#deposit initial amount
account1.deposit(1000)

#withdraw some amount
account1.withdraw(400)

#display updated amount information
account1.display()
