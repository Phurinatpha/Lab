import math
n = int(input())

def rotate(n):
    digs = int(math.log10(n))
    x = (10 ** digs) * (n % 10) + n // 10
    return x 
