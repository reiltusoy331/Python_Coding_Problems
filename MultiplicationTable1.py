# Write a Python program that prints the multiplication table for a positive integer n.
# The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).
# Use a loop to implement your solution.

user_input = int(input("Enter the value of \"n\": "))

total=0
print(f"\n==== Multiplication Table of {user_input} ====")
for i in range(1,11):
    total= user_input * i
    print(f"{user_input} x {i} = {total}")