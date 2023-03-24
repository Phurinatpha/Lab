import math

n = int(input())
ans = math.factorial(n)*(1/math.factorial(n-5) - 1/math.factorial(n-4) + 1/math.factorial(n-3) - 1/math.factorial(n-2) + 1/math.factorial(n-1) - 1/math.factorial(n))

print(int(ans)%(10**6+7))
