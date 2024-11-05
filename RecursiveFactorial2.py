
def RecursiveFactorial(n):
    if n == 0 or n == 1:
        return n
    
    else:
        return n * RecursiveFactorial(n-1)
    

print(RecursiveFactorial(5))