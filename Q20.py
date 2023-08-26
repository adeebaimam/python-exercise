#Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
n=int(input("enter number: "))
while True:
    num_input=int(input("""
          Enter 
          1.for conversion from cm to ft
          2.for conversion from kl to miles
          3.for conversion from usd to inr
          4.for exit
          """))

    if num_input==1:
        ft=0.0328084*n
        print(f'{n}cm = {ft}ft')
    elif num_input==2:
        miles=0.6213712*n
        print(f'{n}km = {miles}miles')
    elif num_input==3:
        inr=82.63*n
        print(f'{n}usd = {inr}INR')
    elif num_input==4:
        print("exit")
        break
    else:
        print("enter valid input")
