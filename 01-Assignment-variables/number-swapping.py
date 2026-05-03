#Basic Variable Swapping
# 1. Switch values of two integers
# Input:  n1 = 20, 
# n2 = 30 
# Output:  n1 = 30 n2 = 20 

n1=20
n2=30
temp = n1
n1=n2
n2 = temp
print("n1 =", n1)
print("n2 =", n2)

#2. Switch values of two strings (characters) 
# Input: char1 = "hello" 
# char2 = "java" 
# Output:  char1 = "java" char2 = "hello"

char1 = "hello"
char2 = "java"
temp = "hello"
char1 = char2
char2 = temp
print("char1 =", char1)
print("char2 =", char2)

# 3. Switch one string value with one integer value
# Input:  n1 = 200,  
# char2 = "java" 
# Output:  n1 = "java" char2 = 200 


n1 =200
char2 = "java"
temp = n1
n1 = char2
char2 = temp
print("n1 =", n1)
print("char2 =", char2)


# Banking and Transactions 

# 5. Update balance after deposit Initial balance: 
# current_balance = 10000 
# Deposit amount: deposit_balance = 5000 
# Output: ○ Before deposit: 
# current_balance = 10000 ○ After deposit: current_balance = 15000 


current_balance = 10000
deposit_balance = 5000
after_deposit = current_balance + deposit_balance
print("current_balance =", current_balance, "After Deposit Total Balance =", after_deposit)


# 6. Update balance 
# after withdrawal Before: balance = 12000
# Withdrawal: 3000 
# After: ? 

before_balance = 12000
withdrawal = 3000
After = before_balance - withdrawal
print("after withdrawal Before: balance =", before_balance, "After balance is =", After)


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


