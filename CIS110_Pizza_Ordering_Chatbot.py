#Design a pizza ordering chatbot for users to build a pizza order, specifying size, flavor, crust type, quantity, method to receive and also displays accurate price.*****
print("Bienvenido, it-sa me, Mario your-a virtual assistant. I will help you-a order a plumber! OH No-ho-ho-ho!, I mean a pizza-pie!")
print("I-ma going to ask-a you a few-a questions. After typing an answer, press-a enter.")

#User enters name, field cannot be left blank, identify me as creator.*****
userName = input("\nPlease-a Enter your-a name:  ")
while len(userName) == 0:
    userName = input("Oh-a No! Name cannot-ta be blank! Please-a, enter your name:  ")
if userName.lower() == "justin":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. It-sa nice to meet you!")
    
#User enters size, field cannot be left blank, entry must be recognized by application.*****
size = input("\nNow, tell-a me what size-a do you want? Enter small, medium, or-a large:  ")
while size.lower() not in ["small", "medium", "large"]:
    size = input("Oh-a No! Invalid value! Please-a enter small, medium, or-a large:  ")
    
#User enters flavor, field cannot be left blank.*****
flavor = input("\nHere we-a go! Now, Enter the flavor of-a pizza:  ")
while len(flavor) == 0:
    flavor = input("Oh-a No! Flavor cannot be blank! Please-a enter a flavor:  ")
    
#User enters crust type, field cannot be left blank.*****
crustType = input("\nYahoo! Now, What type of-a crust do you-a want:  ")
while len(crustType) == 0:
    crustType = input("Oh no! Crust type cannot be-a blank! Please-a enter crust type:  ")

#User enters quantity, field must be a numeric value.*****
quantity = input("\nYipee! How many of these-a pies do you want to-a order? Enter a numeric value:  ")
while not quantity.isdigit():
    quantity = input("\nOh-a No! Value not-a recognized. Please-a enter a numeric value:  ")
quantity = int(quantity)

#User enters method for receiving order, entry must be recognized by application, for delivery orders add $5 fee.*****
method = input("\nIs-a this carry out or delivery:  ")
while method not in ["carry out", "delivery"]:
    method = input("Oh-ho-ho No! Invalid value! Please-a enter carry out or delivery:  ")
    
#Delivery Fee.*****
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
    
#Sales Tax.*****
salesTax = 1.1

#Pricce per piza.*****
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
    
#Total cost of pizza.******
total = (pizzaCost * quantity) * salesTax + deliveryFee

#Order summary, Thank user for order.*****
print("-" * 10)
print(f"Thank-a you, {userName}, for your-a order.")
print(f"Your-a {quantity} {size} {flavor} pizza pie(s) with {crustType} crust-a costs ${total:,.2f}.")

#Coupon Statement.*****
if total >= 50:
    print("\nWhoo-A-Hoo! Congratulations! You've been awarded a $10 off-a coupon for your-a next order!")
else:
    print("\nOrder over-a $50 will receive a free $10 off-a coupon!")
    
#End of application dialog.
print("-" * 10)