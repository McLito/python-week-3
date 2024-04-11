#1.
def calculate_discount(price, discount_percent):
  discount = price * (discount_percent/100)
  if discount_percent >= 20:
    final_price = price - discount
    return (final_price)
  else:
    return(price)
  
#2.
price= float(input("enter the item's price: "))
discount_percent= float(input('enter the discount percentage: '))
print('final price of item is: '+ str(calculate_discount(price, discount_percent)))
