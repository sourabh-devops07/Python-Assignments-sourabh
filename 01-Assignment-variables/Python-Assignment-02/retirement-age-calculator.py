# 3. Task: Retirement Age Calculator 
# ● Objective: Write a program that prompts the user for their age and tells them how many years until they reach retirement age (65). 
# ● Hints: 
# ○ Ask the user to input their age. 
# ○ Calculate how many more years they have until they reach 65 years of age. 
# ○ Display the number of years left until retirement or a message if the user has already reached retirement age.

age = int(input("Enter Your Age - "))
if age < 65:
    year_left = 65 - age
    print(f" you have {year_left} years left until Retirement")
else:
    print("You has already reached retirement age")
