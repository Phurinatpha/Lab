#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640610676
# Lab 04
# Problem 4
# 204111 Sec 002

def round_to_int(x):
    # WRITE YOUR CODE HERE
   
    if (x>0):#plus case
        num = (x*10)%10
        if (num>=5):
            x = (x+1)
        else:
            x = (x)
    else:   #minus case
        num = (abs(x)*10)%10
        if (num>=5):
            x = (x-1)
        else:
            x = (x)
    return int(x)

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(round_to_int(x))

if __name__ == '__main__':
    main()
