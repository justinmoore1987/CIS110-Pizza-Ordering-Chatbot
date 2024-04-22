#A little something extra.
print(" __        __   _                            _          ____  _                 ____ _           _     ____        _   ")
print(" \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  _ \(_)__________ _   / ___| |__   __ _| |_  | __ )  ___ | |_ ")
print("  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |_) | |_  /_  / _` | | |   | '_ \ / _` | __| |  _ \ / _ \| __|")
print("   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  __/| |/ / / / (_| | | |___| | | | (_| | |_  | |_) | (_) | |_ ")
print("    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|   |_/___/___\__,_|  \____|_| |_|\__,_|\__| |____/ \___/ \__|")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")                                                                                                                      

#Design a pizza ordering chatbot for users to build a pizza order, specifying size, flavor, crust type, quantity, method to receive and also displays accurate price.*****
print("Bienvenido, it-sa me, Mario your a-virtual assistant. I will help a-you order a plumber! OH No-ho-ho-ho!, I mean a pizza-pie!")
print("I-ma going to ask a-you a few a-questions. After typing an answer, press-a enter.")

#User enters name, field cannot be left blank, identify me as creator.*****
userName = input("\nPlease-a Enter your a-name:  ")
while len(userName) == 0:
    userName = input("Oh a-No! Name cannot a-be blank! Please-a, enter your a-name:  ")
if userName.lower() == "justin":
    print(f"\nMy creator, {userName}. Pleasure to a-serve you!")
else:
    print(f"\nHello, {userName}. It-sa nice to a-meet you!")
    
#Checkpoint spot for where to start if there is another order after initial order.
keepGoing = "y"
while keepGoing.lower() == "y":
    
    #User enters size, field cannot be left blank, entry must be recognized by application.*****
    size = input("\nNow, tell a-me what size a-do you want? Enter small, medium, or-a large:  ")
    while size.lower() not in ["small", "medium", "large"]:
        size = input("Oh a-No! Invalid value! Please-a enter small, medium, or-a large:  ")
    
    #User enters flavor, field cannot be left blank.*****
    flavor = input("\nHere we a-go! Now, Enter the flavor of a-pizza:  ")
    while len(flavor) == 0:
        flavor = input("Oh a-No! Flavor cannot a-be blank! Please-a enter a flavor:  ")
    
    #User enters crust type, field cannot be left blank.*****
    crustType = input("\nYahoo! Now, What type of a-crust do you-a want:  ")
    while len(crustType) == 0:
        crustType = input("Oh a-No! Crust type cannot a-be blank! Please-a enter crust type:  ")

    #User enters quantity, field must be a numeric value.*****
    quantity = input("\nYipee! How many of these a-pies do you want to-a order? Enter a numeric value:  ")
    while not quantity.isdigit():
        quantity = input("\nOh a-No! Value not-a recognized. Please-a enter a numeric value:  ")
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
    print(f"Thank a-you, {userName}, for your-a order.")
    print(f"Your-a {quantity} {size} {flavor} pizza pie(s) with {crustType} crust-a costs ${total:,.2f}.")

    #Coupon Statement.*****
    if total >= 50:
        print("\nWhoo-A-Hoo! Congratulations! You've been awarded a $10 off a-coupon for your-a next order!")
    else:
        print("\nOrder over-a $50 will receive a free $10 off a-coupon!")
        print("-" * 10)

    #Order received and add a countdown timer for when the order is ready.
    print("Your-a order has a-been received! ETA 3 minutes!")
    for min in range(3, 0, -1):
        print(min, "minutes to a-go")
        for seconds in range(60, 0, -1):
            print(seconds, end = "\r")
            import time
            time.sleep(1)
    print("Order is a-ready!")
    
    #Ask the customer if they would like anotther order and continue from the top checkpoint.
    keepGoing = input("Do you a-want to place another order? Enter y or n:  ")
    while keepGoing.lower() not in ["y", "n"]:
        keepGoing = input("OH A-NO! Invalid value: Enter y or n:  ")
       
#A little something extra.
print(" _______ _                 _     __     __         _ ")
print(" |__   __| |               | |    \ \   / /        | |")
print("    | |  | |__   __ _ _ __ | | __  \ \_/ /__  _   _| |")
print("    | |  | '_ \ / _` | '_ \| |/ /   \   / _ \| | | | |")
print("    | |  | | | | (_| | | | |   <     | | (_) | |_| |_|")
print("    |_|  |_| |_|\__,_|_| |_|_|\_\    |_|\___/ \__,_(_)")