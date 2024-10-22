# Description:
# Write a Python program that prints a pyramid pattern made with asterisks.
# The number of rows should be determined by the value of the variable n. 
# This value will be entered by the user.
# You may assume that the value of n is a positive integer.


num = int(input("Enter the value of \"n\": "))


#space
for i in range(1,num+1):
    print("  "*(num-i),end=" ")

    #asterisk
    for j in range(i):
        print(" *",end='')

    print()
    

