# 32.If user input is: 
# Name: Dev 
# Age: 25 
# City: Jaipur 
# Hobby: Cooking 
# Then 
# Output is : Meet Dev, a 25-year-old enthusiast from Jaipur. 
# When not busy 
# with daily tasks, Dev loves spending time cooking. Life in Jaipur keeps Dev energetic and curious every single day. With coding as a passion, the future looks creative and inspiring for Dev in the Jaipur City. 

Name = "Dev"
Age = 25
City = "Jaipur"
Hobby = "Cooking"
print(F"Meet {Name}, a {Age}-year-old enthusiast from {City}. When not busy with daily tasks, {Name} loves spending time {Hobby}. Life in {City} keeps {Name} energetic and curious every single day. With coding as a passion, the future looks creative and inspiring for {Name} in the {City} City. ")

# 33.Create a Python program that asks the user for the following: 
# ● Full Name 
# ● Profession 
# ● Favorite Quote 
# ● Years of Experience Output format: ------------------------------------------------ Name        
# : <Full Name> Profession  : 
# <Profession> Experience  : 
# <Years of Experience> years

full_name = input("Enter your Full Name : ")
professional = input("Enter your Profession : ")
years_exp = input("Enter your Experience : ")
print(F" Name :-  {full_name}")
print(F" Profession :-  {professional}")
print(F" Experience :-  {years_exp}")


# 34.Ask the user: 
# ● Movie Name ● 
# Viewer Name ● 
# Seat Number ● 
# Show Time Output format: 
# 🎬 Movie Ticket 🎟 ------------------------ Movie   
# : <Movie Name> Name    : 
# <Viewer Name> Seat No : 
# <Seat Number> Time    : 
# <Show Time> Enjoy the show! 
 
 
movie_name = input("Enter Movie Name -")
viewer_name = input("Enter Viewer Name -")
seat_number = input("Enter Seat Number -")
show_time = input("Enter show time -")

print(F" 🎬 Movie Ticket 🧧 ")
print("Movie Name", movie_name)
print("Viewer Name", viewer_name)
print("Seat Number", seat_number)
print("Show Time", show_time)
print("Enjoy the Show!")
