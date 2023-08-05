#Exercise 1B: Create a string made of the middle three characters
def middle_three_char(input_string):
    mystr = len(input_string)
    #get middle index no.
    middle_index =int(mystr/2)
    
    #if input_string is odd
    if mystr%2==1:
        #ex = mystr[::]
        middle_chars = input_string [middle_index - 1:middle_index + 2]
    else:
        middle_chars = input_string [middle_index - 1:middle_index + 2]
    return(middle_chars)

print(middle_three_char("JhonHasHand"))
