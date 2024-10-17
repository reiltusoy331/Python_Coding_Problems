#--------------
# Option 2
#--------------

num =int(input("Enter an integer: "))

if num==0 or num==1:
    print("Not Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
