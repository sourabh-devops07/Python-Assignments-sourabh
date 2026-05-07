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