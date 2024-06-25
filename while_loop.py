no_of_coins = 6

while no_of_coins > 0:
    print(no_of_coins)
    no_of_coins = no_of_coins - 1
else:
    print("No coins in the piggy bank")




# Initialise the variable. This means set a name for the variable and add a value:
bank_balance = 1000

# Set the loop, what to do and when to stop:
while bank_balance >= 100:
    print(f"Your bank balance is {bank_balance}")
    bank_balance -= 100
else:
    print(f"Your balance is too low. Make a deposit")