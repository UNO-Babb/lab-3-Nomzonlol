#TempConvert.py
#Name:Nomaan Ahmed 
#Date:2/9/25
#Assignment:Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = 75

  tempC = round((tempF - 32) * 5 / 9)

  print(f"{tempF} degrees Fahrenheit is {tempC} degrees Celsius.")
if __name__ == '__main__':
  main()
