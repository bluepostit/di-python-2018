# Bar calculator
customer_name = input("What is the customer's name? ")
waiter_name = input("What is the waiter's name? ")
item_name = input("What is the name of the item ordered? ")
price = input("What is the price of 1 " + item_name + "? ")
amount_of_items = input("How many " + item_name + "s were ordered? ")
discount = input("What is the discount amount? ")

# Calculate total
total = (int(price) * int(amount_of_items)) - int(discount)

# Bonus: add VAT
vat_percent = 17
vat = total * vat_percent / 100
total = total + vat

# Output
line_border = '-' * 40
print('{}\n'
    '- Thank you for your business, {}!\n'
    '{}\n'
    '- {} x{}\n'
    '-     @ {}\n'
    '- Discount: {}\n'
    '- VAT: {}\n'
    '- TOTAL: {}\n'
    '{}\n'
    '- Your waiter was {}\n'
    '{}\n'
    .format(line_border, customer_name, line_border, item_name,
        amount_of_items, price, discount, vat, str(total),
        line_border, waiter_name, line_border)
    )
