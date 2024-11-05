
def RecursiveFactorial(n):
    if n <= 1:
        return n
    
    else:
        return n * RecursiveFactorial(n-1)
    

print(RecursiveFactorial(5))