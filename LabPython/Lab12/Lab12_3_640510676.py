#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 12
# Problem 3
# 204111 Sec 002

def is_prime(n ,i = 2):    
    if i * i > n or n==2: 
        return True 
    if (n < 2): 
        return False
    if (n % i == 0): 
        return False
    
    return is_prime(n, i + 1) 

def main():
    print(is_prime(51))

if __name__ == '__main__':
    main()

