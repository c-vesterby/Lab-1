#
# Christine Vesterby
# Jan 15 2022
# This program converts a user-entered Celsius temperature and
# converts it to Fahrenheit
#

# Get the Celsius temperature.
celsius = float(input('Enter a Celsius temperature: '))

# Calculate the Fahrenheit equivalent.
fahrenheit = ((9.0 / 5.0) * celsius)+ 32

# Display the Fahrenheit temperature.
print(f'That is equal to {fahrenheit:.2f} degrees Fahrenheit.')