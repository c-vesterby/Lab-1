#
# Christine Vesterby
# Jan 15 2022
# This program converts a user-entered Fahrenheit temperature and
# converts it to Celsius
#

# Get the Fahrenheit temperature.
fahrenheit = float(input('Enter a Fahrenheit temperature: '))

# Calculate the Celsius equivalent.
celsius = (5.0 / 9.0) * (fahrenheit - 32)

# Display the Celsius temperature.
print(f'That is equal to {celsius:.2f} degrees Celsius.')