# Write a Python program that prints the smallest of three integers a, b, and c.

##########
# Option 1
##########

a=-1
b=-3
c=-4

if (a < b) and (a < c):
    print(a)

elif (b < a) and (b < c):
    print(b)

else:
    print(c)
