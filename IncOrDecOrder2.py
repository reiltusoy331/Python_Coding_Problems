# Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.
# If a > b > c, print "Decreasing Order".
# If a < b < c, print "Increasing Order".
# Else, print "None". 

##########
# Option 2
##########
a=3
b=2
c=1

if a < b  < c:   # comparison chaining
    print("Increasing Order.")

elif a > b > c: # comparison chaining
    print("Decreasing Order.")

else:
    print("None")