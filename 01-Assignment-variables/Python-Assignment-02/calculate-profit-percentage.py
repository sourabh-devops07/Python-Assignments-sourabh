# 1. Task: Calculate Profit Percentage 
# ● Write a program that takes input for the cost price and selling price of an item. 
# ● Hints 
# ○ Prompt the user to input the cost price and selling price. 
# ○ Determine whether the transaction resulted in a profit or loss. 
# ○ If there is a profit calculate the profit percentage; if there is a loss calculate the loss percentage. 
# ○ Display the profit or loss and the respective percentage

cost_price =int(input("Enter the Cost Price -"))
selling_price=int(input("Enter the selling price -"))
if cost_price>selling_price:
    loss = cost_price - selling_price
    loss_percentage = loss/cost_price*100
    print(f" Loss - {loss}")
    print(f" Loss Percentage - {loss_percentage}")
elif cost_price<selling_price:
    profit= selling_price - cost_price
    profit_percentage = profit/cost_price*100
    print(f" Profit - {profit}")
    print(f" Profit Percentage - {profit_percentage}")
else:
    print("No profit No Loss")
