# 5. Task: Salary Calculation 
# ● Objective: You have to calculate an employee's salary by computing the gross salary tax and net salary based on the given parameters. 
# ● Hints: 
# ○ Base Salary = ₹50000 
# ○ Bonus = ₹5000 
# ○ Tax Rate = 10%  
# ○ Other Charges = ₹2000 Display the Gross Salary Tax and Net Salary. 
#base_salary = 50000
sal=int(input("Enter your salary: "))
bonus=int(input("Enter your bonus: "))
other_ch=int(input("Enter other charges: "))
tax_r=10
gross_sal=sal+bonus-other_ch
income_tax=(gross_sal*tax_r)/100
net_sal=gross_sal-income_tax
print(f"""Gross Salary Tax = {income_tax}
Net Salary = {net_sal}""")
