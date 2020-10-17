#Python program to convert temperature from Fahrenheit to Kelvin 
#Link to Repository Path:https://github.com/KR031994/bch5884.git
import sys
print("Please enter a temperature in Fahrenheit: ")
Fahrenheit=float(sys.stdin.readline())
Kelvin=273.5 + ((Fahrenheit - 32.0) * (5.0/9.0))
print("The corresponding Kelvin temperature is:",(Kelvin))
