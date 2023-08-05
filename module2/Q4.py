#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
#s1 = "America"
#s2= "Japan"
#AJrpan
s1 = "America"
s2 = "Japan"
# get first character from both string
f = s1[0] +s2[0]
#get mid index of both string
m_s1 = int(len(s1)/2)
m_s2 = int(len(s2)/2)
#get mid character of both string
m_c_s1 = s1[m_s1]
m_c_s2 = s2[m_s2]
m = m_c_s1 + m_c_s2
#get last char of both string
l = s1[-1]+s2[-1]
#to get new string  
new_str = f+m+l
print(f+m+l)
