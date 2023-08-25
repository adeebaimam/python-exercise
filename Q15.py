'''
Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)      WEATHER

      >= 30                             >=90                Hot and Humid
      >= 30                             < 90                Hot
      <30                               >= 90               Cool and Humid
      <30                               <90                 Cool
'''
T=int(input("Temperature: "))
H=int(input("Humidity: "))
if T>=30 and H>=90:
    print("Hot and Humid")
elif T>=30 and H<90:
    print('Hot')
elif T<30 and H>=90:
    print('Cool and Humid')
elif T<30 and H<90:
    print('Cool')
