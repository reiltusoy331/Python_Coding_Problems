# Write a Python program that simulates an interactive calculator with the basic arithmetic operations 
# in Python (addition, subtraction, multiplication, division, integer division, and modulo).
# The program must interact with the user by asking for the values and the type of operation 
# that will be performed.
# The output should include the values, the operation, and the result (as shown below).
# The type of operation will be denoted by an integer.
# - 1 for addition 
# - 2 for subtraction
# - 3 for multiplication
# - 4 for division
# - 5 for integer division
# - 6 for modulo
# The program should present an initial message to the user describing the types of operations and 
# the integer that has to be entered to select each one of them.
# If the values entered by the user are invalid for the operation selected, 
# a descriptive message should be displayed. For example, for a division operation the denominator cannot be 0.
# If the user enters an invalid integer to select the operation, print "Please choose a valid operation"

print("=== Welcome to your Interactive Python Calculator ===\n")

num1=int(input("Please enter the first value:"))
num2=int(input("Please enter the second value:"))
print("Great! Now enter the operation.\n")
print("These are the available options:\n")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")
operator=int(input("--> Enter the corresponding integer: "))

if operator == 1:
    result=num1+num2
    print(f"The result of {num1} + {num2} is {result}.")

elif operator == 2:
    result=num1-num2
    print(f"The result of {num1} - {num2} is {result}.")

elif operator == 3:
    result=num1*num2
    print(f"The result of {num1} * {num2} is {result}.")

elif operator == 4:
    result=num1/num2
    print(f"The result of {num1} / {num2} = {result}.")

elif operator == 5:
    result=num1//num2
    print(f"The result of {num1} // {num2} is {result}.")

elif operator == 6:
    result=num1%num2
    print(f"The result of {num1} % {num2} is {result}.")

else:
    print("Please choose a valud operation.")