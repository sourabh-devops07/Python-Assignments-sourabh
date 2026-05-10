# 14. Arranging Three Numbers in Descending Order 


a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))
  
numbers=[a,b,c]
numbers.sort(reverse=True)

print("The numbers is decending order is",numbers)


numbers.sort(reverse=False)
print("The numbers in ascending order are",numbers)