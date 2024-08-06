# Declare a variable name "num_row" 
# The said variable will dictate the number of rows of the triangle pattern
### Target Output ###
#        *
#      * *
#    * * *
#  * * * *

num_row = 4

for i in range(num_row):
    #space
    for space in range(num_row-i):
        print(" ",end=' ')
    #star
    for star in range(i+1):
        print("* ",end='')
    print()