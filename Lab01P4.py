#
# Christine Vesterby
# Jan 15 2022
# This program calculates the amount a customer will pay for purchasing books from Bargain Used Books.
#

paperback = 2.5
hardcover = 7.0
magazine = 3.95
tax = 0.07

# Input entered from the customer, regarding what books they are purchasing and how many.
amount_pap = float(input('Enter the number of paperback books: '))
amount_hard = float(input('Enter the number of hardcover books: '))
amount_mag = float(input('Enter the number of magazines: '))

# Processing the amount they will pay for the books they are purchasing. 
subtotal = (amount_pap * paperback) + (amount_hard * hardcover) + (amount_mag * magazine)
sales_tax = subtotal * tax
full_cost = subtotal + sales_tax

# Output of the subtotal, sales tax, and full cost the customer will pay. 
print(f'Cost before tax: ${subtotal:.2f}')
print(f'Sales tax: ${sales_tax:.2f}')
print(f'Cost after tax: ${full_cost:.2f}')