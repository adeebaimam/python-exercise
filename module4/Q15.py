#working of an atm machine
class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        
        self.menu()
        
    def menu(self):
            
        user_input=input("""
                     How will you proceed
                     Enter 1.To create pin
                     Enter 2.To check balance
                     Enter 3.To deposit cash
                     Enter 4.To withdraw money
                     Enter 5.To exit""")
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.check_balance()
        elif user_input == '3':
            self.deposit()
        elif user_input == '4':
            self.withdraw()
        else:
            print('bye')
    def create_pin(self):
        self.pin=input("enter your pin")
        print("pin set successfully")
        
   
            
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            self.balance=self.balance+amount
            print('deposited successfully')
        else:
            print('invalid pin')
            
             
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount to withdraw "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("balance debited successfully")
            else:
                print("insufficent balance")
        else:
            print('invalid pin')
            
            
    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(f'your current balance is : {self.balance}')
                        
        else:
            print('invalid pin')
            
    
    


