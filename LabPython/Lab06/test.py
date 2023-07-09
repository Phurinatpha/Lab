#!/usr/bin/env python3
# ชิกานดา ณ มณี
# 640510610
# Lab 06
# Problem 2
# 204111 Sec 00

def int_to_bin(x):
    result = 0
    i = 0
    while (int(x) != 0): 
        r = int(x)%2
        result = result + (r*10**i)
        x = int(x/2)
        i += 1
    return result
def float_y(x):
    float_x = abs(float(x)-int(x))
    a = 1
    result_ = 0
    if (float_x == 0):
        return 0
    while (float_x != 1):
        float_x = float_x * 2
        bina = float_x//1
        result_ = result_ + (bina*(10**-a))
        if float_x > 1:
            float_x = float_x - 1
        else:
            float_x = float_x    
        a +=1
    return result_

def float_to_bin(x):
    if(x<0):
        base = (float(int_to_bin(x)) + float_y(x))*-1
    else:
        base = (float(int_to_bin(x)) + float_y(x))
    return float("%.6f" %base)
def main():
    x = float(input())
    #print("{:.6f}".format(float_to_bin(x)))

    print(float_to_bin(x))

if __name__ == '__main__':
    main()