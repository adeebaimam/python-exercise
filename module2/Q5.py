#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
word = "usa"
#convert strings into upper case
string = str1.upper() 
#count uppercase word from the string 
print(string.count(word.upper()))
