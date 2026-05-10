# 6. Task: Bank Loan Approval System 
# ● Objective: You have to create a javascript script that checks whether an user is eligible for a bank loan based on various criteria.
# ● Hints: 
# ○ The applicant's age must be between 18 and 60 years. 
# ○ The applicant's monthly income must be greater than or equal to ₹25000. 
# ○ The applicant's credit score must be greater than or equal to 700. 
# ○ The applicant must not have any outstanding debts greater than ₹10000 1. Output: 
# ○ Display "Loan Approved" if the applicant meets all the conditions.
# ○ Otherwise display "Loan Rejected".

a=int(input("Enter Applicant Age :"))
b=int(input("Enter Applicant monthly income :"))
c=int(input("Enter applicant credit score :"))
d=int(input("Enter applicant outstanding debt :"))
if a>=18 and a<=60:
    print("cleared age criterion")
    if b>=25000:
        print("cleared income criterion")
        if c>=700:
            print("cleared credit score criterion")
            if d<=10000:
                print("Congratulations You are Eligible for loan")

else:
    print("You are not eligible for loan hence loan rejected") 