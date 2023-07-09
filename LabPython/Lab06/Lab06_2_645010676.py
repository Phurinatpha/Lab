#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 06
# Problem 2
# 204111 Sec 002

def deci_x(x): #copy e lab 
    result = 0
    i = 0
    while (int(x) != 0):
        r = int(x)%2
        result = result + r*10**i #บวกค่าไปทีละหลักตามยกกำลัง i 
        x = int(x/2)
        i += 1
    return result

def float_x(x): #นำ def deci มาเปลง
    y = abs(float(x) - int(x)) #ให้คิดแค่ค่าหลัง .
    res = 0 
    i = 1
    if (y==0): #ถ้า y เป็น 0 
        return 0
    else: pass 
    while (y != 1): 
        y = (y*2)
        r = y//1
        res = res + r*10**-i #บวกค่าไปทีละหลักตามยกกำลัง -i(ค่าหลังจุดทศนิยม)
        if (y>1):   #ตัดค่าที่เกินออกเพราะการนำไปคิดต่อ y ต้อง <1
            y = y-1
        else:       #ให้ค่า y มีค่าเท่าเดิม
            y = y
        i += 1      #ค่ายกกำลัง
    return res

def float_to_bin(x):
    if (x>=0):
        sumxx = float_x(x) + deci_x(x)
    else:
        sumxx = (float_x(x) + deci_x(x))*-1
    return float('{0:.6f}'.format(sumxx))

def main():
    x = float(input())
    print(float_to_bin(x))

if __name__ == '__main__':
    main()