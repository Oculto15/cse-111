from datetime import datetime

# Set variables 
disc = 0.1
taxes = 0.06
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
discount = 0

# Ask about the subtotal
sub_total = float(input("Please enter the subtotal: "))

# Use if statement to specify the requirements to get the discount
if sub_total >= 50 and (day_of_week == 1 or day_of_week == 2):
    
    # Calculate discount
    discount = sub_total * disc
    print(f"Discount amount: {discount:.2f}")
    
    # Calculate sales tax
    sub_total -= discount
    sales_tax = (sub_total * taxes)
    print(f"Sales tax amount: {sales_tax:.2f}")

    #Calculate total
    total = sub_total + sales_tax
    print(f"Total: {total:.2f}")
    print()

# Calculate total for prices below $50
sales_tax = sub_total * taxes
print(f"Sales tax amount: {sales_tax:.2f}")
total = sub_total + sales_tax
print(f"Total: {total:.2f}")
print()