# 12. Calculate profit or loss percentage Input: 
# cost_price = 500, 
# selling_price = 600 
# Output: Profit or Loss = ? 

cost_price = 500
selling_price = 600 
profit = selling_price - cost_price
profit = profit / cost_price * 100
print(F" Profit - {profit}")
Loss = cost_price - selling_price
Loss = Loss / selling_price * 100
print(F" Loss - {Loss}")

# 13. Calculate simple interest 
# Input: principal = 10000, 
# rate = 5, 
# time = 2 
# Output: Simple Interest = ? 

principal = 10000
rate = 5
time = 2
SI = principal * rate * time /100
print(F"Simpe Intrest - {SI}")

# 14. Calculate compound interest Input: 
# principal = 10000, 
# rate = 5, 
# time = 2 
# Output: Compound Interest = ?

principal = 10000
rate = 5
time = 2
Total_amount = 10000*(1+5/100)**2
CI = Total_amount - principal
print(F"Compound Interest - {CI}")
