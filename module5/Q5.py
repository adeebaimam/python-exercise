#Convert string into a datetime object
from datetime import datetime
date_string = "Feb 25 2020 4:20PM"

#to convert string into date time object .sprtime function is used
#%b-month name,%d-date of a month,%Y-year,%I-hour(01-12),%p-am,pm

datetime_object=datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print(datetime_object)
