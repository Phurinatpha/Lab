n = int(input())
k = (n*2 - 4*n**2*a*2)/(4*a*2 - 1)
a = (n - (n*2 + 4*k)**0.5)/(2*n)
min_val = a*3/(1-b) + b*2/(1-a)
print(f"{min_val:.8f}") # prints the result with 8 decimal places