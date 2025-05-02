#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

shipping_cost = 5
order_total = int(input("What is the total amount for your order? $ "))

if order_total > 50:
    print(f"Your order total is ${order_total} with free shipping!")
else:
    print(f"Your order total is ${order_total} plus ${shipping_cost} for shipping, totaling ${order_total + shipping_cost}!")