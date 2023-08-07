#Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
letters = 0
digits = 0
special_symbol = 0
print("total count of letters,digit and special symbol :")
for i in str1:
    if i.isalpha():
        letters +=1 
    elif i.isdigit():
        digits +=1
    else:
        special_symbol +=1
print("letters =", letters,"digits =", digits,"special_symbol =",special_symbol)     
        
