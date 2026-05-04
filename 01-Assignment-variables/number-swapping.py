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
print(F"n1 = {n1}")
print(F"char2 = {char2}")



