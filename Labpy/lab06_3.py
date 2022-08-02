#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 4
# 204111 Sec 002

def  base_b(x, b, k=0):
    if x//b == 0 : 
        return (x%b)*10**k
    else:
        return base_b(x//b,b,k+1) + (x%b)*10**k
        

def main():
    x = int(input())
    b = int(input())
    print(base_b(x,b))
    main()


if __name__ == '__main__':
    main()
