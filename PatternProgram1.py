# Declare a variable name "num_row" 
# The said variable will dictate the number of rows of the triangle pattern
### Target Output ###
#       *
#      * *
#     * * *
#    * * * *

num_row = 4

for i in range(1,num_row+1):
    #space
    for space in range(num_row-i+1):
        print(" ",end='')
    #star/asterisk
    for star in range(i):
        print("* ",end='')
    print()






