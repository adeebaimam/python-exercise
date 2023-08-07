#Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = 'PYnaTive'
print("word =",str1)
lower = []
upper = []
for chars in str1:
    if chars.islower():
        #adding characters at last
        lower.append(chars)
    else :
        upper.append(chars)
        #joing both lower and upper
new_string = "".join(lower+upper)
    
print(new_string)
