### Target Output ###
#  * * * *
#    * * *
#      * * 
#        * 

asterisk = 4

for i in range(asterisk):
    for j in range(i):
        print(" ",end=' ')    
    for j in range(i,asterisk):
        print("* ",end='')
    print()

asterisk = 5

for i in range(asterisk):
    for j in range(i,asterisk):
        print(" ",end='')    
    
    for j in range(i):
        print("*",end='')
    
    for j in range(i+1):
        print("*",end='')
    print()