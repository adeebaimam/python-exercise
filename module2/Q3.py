#Exercise 2: Append new string in the middle of a given string
#s1 = "Ault"
#s2 = "Kelly"
s1 = "ault"
s2 = "kelly"
length_s1 = len(s1)
mid_s1 = int(length_s1/2)
front_char_s1 = s1[:mid_s1]
back_char_s1 = s1[mid_s1:]
#append two string by cocatenation
app_s2 = front_char_s1+s2+back_char_s1
print(app_s2)
