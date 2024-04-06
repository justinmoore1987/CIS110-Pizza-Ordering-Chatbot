print("Hey there! I'm Justin! As in Just-In time to take you on a Pizza Masterpiece Making Adventure! Lets get started so you can order and enjoy your pizza creation! ")
print("I have just a few simple questions for you so I know just how you like your pizza and everything you'd like to have on it! Just respond and hit 'Enter' so I receive your instruction! It is that simple!")
userName = input("\nEnter your name so I know what to call you:  ")
print(f"\nHello, {userName}, it is my pleasure to be making your pizza just the way you like!")
size = input("\nWhat size are you needing? Small? Medium? Large?  ")
quantity = input("\nHow many pizza's are you looking to get? Please tell me a number:  ")
quantity = int(quantity)
flavor = input("\nPlease let me know what flavor or type of pizza you are craving today:  ")
crustType = input("\nMy favorite part, the CRUST! How would you like your crust to be? Choose wisely and tell me your decision:  ")
method = input("\nWould you like to come on over for Carry-Out? Or have this work of art Delivered?  ")
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print("-" * 10)
print(f"Thank You, {userName}, for your order!")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)