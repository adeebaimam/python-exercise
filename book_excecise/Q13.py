'''
 Write a class to represent a vector (a series of float values). Include member functions to perform the following tasks:

   (a) To create a vector
   (b) To modify the value of a given element
   (c) To multiply by a scalar value
   (d) To display the vector in the form (10, 20, 30, ...)

   Write a program to test your class.
'''

class Vector:
    def __init__ (self):
        self.vector=[]
        self.menu()
            
    def menu(self):
        while True:
            input_menu=print('''
                         What functions do you want to perform
                         1. To create a vector
                         2. To modify the value of a given element
                         3. To multiply it by a scalar value
                         4. To display the vector 
                         5. To Exit
                         ''')
            choice=input("Enter your choice : ")
        
            if choice=='1':
                self.create_vector()
            elif choice=='2':
                self.modify()
            elif choice=='3':
                self.multiply_scalar()
            elif choice=='4':
                self.display()
            elif choice=='5':
                print('Exit program')
                break
            else:
                print('Invalid Number. Please try again')
            
            
    def create_vector(self):
        size=int(input('Enter the size of vector: '))
        print('Enter element')
        value=list(map(int,input().split()))
        self.vector=value
        print('Vector created')
    
    def modify(self):
        index=int(input('Enter the index number you want to modify: '))
        if 0<=index<len(self.vector):
            new_value=int(input(f'Enter the new number to be inserted in place of index: '))
            self.vector[index]=new_value
            print('Element modified')
        else:
            print('Invalid index number, try again')
            
    def multiply_scalar(self):
        scalar_val=int(input('Enter the scalar value: '))
        for i in range(len(self.vector)):
            self.vector[i] *= scalar_val
            
        print('Vector multiplied by scalar')
        
    def display(self):
        print('Vector',self.vector)
        
vector1=Vector()
