'''
Modify the class and the program of Exercise 12 for handling 10 customers.

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
        
        if deposit_amount>0:
            self.balance += deposit_amount
            print(f'Deposited amount = {deposit_amount}\nNew balance = {self.balance}')
        else:
            print(f'Invalid deposit amount. Please enter valid amount')
            
    def withdraw(self,amount):
        
        if withdraw_amount>0:
            if withdraw_amount <=self.balance:
                self.balance -=withdraw_amount
                print(f'Withdraw amount = {withdraw_amount}\nNew balance = {self.balance}')
            else:
                print('Insufficient amount')
        else:
            print('Invalid withdraw amount')
            
            
    def display(self):
            print(f'Account holder {self.name}')
            print(f'Account number {self.account_number}')
            print(f'Account type {self.type_of_account}')
            print(f'Account balance {self.balance}')
                                   
        
customers_account=[]
for i in range(1,11):
    account_name=input('Enter your name: ')
    account_number=int(input('Enter your account number: '))
    account_type=input("Enter account type: ")
    customer=BankAccount(account_name,account_number,account_type)
    customers_account.append(customer)
    
for account in customers_account:
    deposit_amount=int(input("Amount to be deposited: "))
    account.deposit(deposit_amount)
    withdraw_amount=int(input('Amount to withdrew'))
    account.withdraw(withdraw_amount)
    account.display()

   
              
