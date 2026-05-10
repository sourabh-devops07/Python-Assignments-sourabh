# 7. Task: Students Interview Eligibility Checker 

a=int(input("Enter The Academic score of a Student :"))
b=int(input("Enter The Attendence percentage of a Student :"))
c=input("Enter whether the student has participated in Extra Curriculam activities :")
if a>=60 and b>=75:
    print("cleared academic criterion")
    if c=="yes":
        print("You are Eligible for Interview")
else:
    print("You are not Eligible for Interview") 