# Python program to convert temperature from 
# Fahrenheit to Kelvin 
  
# Function to convert temperature 
def Fahrenheit_to_Kelvin(F): 
    return 273.5 + ((F - 32.0) * (5.0/9.0)) 
  
# Driver function 
F = 50
print("Temperature in Kelvin ( K ) = {:.3f}" 
            .format(Fahrenheit_to_Kelvin( F )))