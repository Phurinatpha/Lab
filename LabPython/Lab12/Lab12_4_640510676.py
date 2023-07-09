#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 12
# Problem 4
# 204111 Sec 002

def series(n):
    if n <2 :
        return n
    elif (n%2==0):
        return 2*(series(n-1)) + 1
    return 2*(series(n-1)) - 1

def main():
    n = 997
    print(series(n))

if __name__ == '__main__':
    main()

#work with 640510662