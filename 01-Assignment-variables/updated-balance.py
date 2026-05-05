# Banking and Transactions 

# 5. Update balance after deposit Initial balance: 
# current_balance = 10000 
# Deposit amount: deposit_balance = 5000 
# Output: ○ Before deposit: 
# current_balance = 10000 ○ After deposit: current_balance = 15000 


current_balance = 10000 
deposit_balance = 5000
print(F"Current Balance : {current_balance}")
print(F"Deposite Balance : {deposit_balance}")

current_balance=current_balance+deposit_balance
print(f"After Deposite : {current_balance}")


# 6. Update balance 
# after withdrawal Before: balance = 12000
# Withdrawal: 3000 
# After: ? 

before_balance = 12000
withdrawal = 3000
print(F"Before Balance : {before_balance}")
print(F"Withdrawal : {withdrawal}")
After = before_balance - withdrawal
print(F"After balance : {After}")


# 7. Increase shopping cart items 
# by 3 
# Before: cart_items = 5 
# After: ?


cart_items = 5
cart_items = cart_items +3
print(cart_items)


# Apply a 20% discount to a price 
# Before: price = 1000 
# After: ? 

price = 1000                                         #20% of 100 = 20/100*1000 = 200
discount = 20                                        # final price = 1000 - 200 =800
final_price = price - (price * discount / 100)
print(final_price)





