
print(" ### Calculate Factorial ### \n")
n = int(input("Enter value of \"n\": "))

factorial = 1    
for i in range(2,n+1):        
    print(f"i = {i} factorial = {factorial}", end=" ")
    factorial *= i
    print(f"new factorial = {factorial}")

