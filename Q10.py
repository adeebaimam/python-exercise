#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
CP=int(input("Enter the cost price: "))
SP=int(input("Enter the selling price: "))
if SP>CP:
    profit=SP-CP
    print("profit=",profit)
else:
    loss=CP-SP
    print("loss=",loss)
