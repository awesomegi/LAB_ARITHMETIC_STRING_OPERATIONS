
price:float = 5.99
quantity:int = 4
tax_rate:float =0.075


subtotal= price*quantity
tax = subtotal*tax_rate
total = subtotal+tax


print("Product Price:",price)
print("Quantity:",quantity)
print("Tax rate:",tax_rate)

print(f"Juice price: ${subtotal}")
print("Tax:",tax)
print("Total:",total)


