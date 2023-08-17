#creating fraction and some operations on farction
class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
        
    def __str__(self):
        return (f'{self.num}/{self.den}')
    
    def __add__(self,other):
        cal_num=self.num*other.den + other.num*self.den
        cal_den=self.den*other.den
        return (f'{cal_num}/{cal_den}')
    
    def __sub__(self,other):
        cal_num=self.num*other.den - other.num*self.den
        cal_den=self.den*other.den
        return (f'{cal_num}/{cal_den}')
    
    def __mul__(self,other):
        cal_num=self.num*other.num
        cal_den=self.den*other.den
        return (f'{cal_num}/{cal_den}')
    
    def __truediv__(self,other):
        cal_num=self.num*other.den
        cal_den=self.den*other.num
        return (f'{cal_num}/{cal_den}')
        
