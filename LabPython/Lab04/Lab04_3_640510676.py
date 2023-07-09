#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 3
# 204111 Sec 002

from re import X


def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
    if p>=1:
        if p+c >=13:
            if p>c:
                return 500*(p+c)//11
            else:
                return 0

        

def main():
    # receive input from user
    p = int(input())
    c = int(input())
    # print result from function
    print(calculate_p2p_evolve_exp(p, c))

if __name__ == '__main__':
    main()