#!#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 1
# 204111 Sec 002

import math
def main():
    x  = int(input("from number:"))
    y  = int(input("to number"))
    print(sum_prime_in_range(x, y))

def is_prime(x):
    div = 2
    while div <= math.sqrt(x):
        if x % div == 0:
            return False
        else:
            if div == 2:
                div = 3
            else:
                div = div + 1
    return True

def sum_prime_in_range(x, y): 
    sumprime = 0                    
    for x in range(x,y+1):          #ลูปจาก x ถึง y+1 เพื่อให้ครบค่า
        if is_prime(x) == True:     #ถ้าเป็น จน เฉพาะรึเปล่า
            sumprime += x           #ให้รวม x ที่เป็น จน เฉพาะ เข้าไปในผลรวม sumprime
        else:                       #กรณีอื่นที่ x ไม่เป็น prime ไม่ต้องนำไปรวม
            sumprime = sumprime     
          
    return int(sumprime)            #นำผลรวม prime ออกมาาาาาาาาา

if __name__ == '__main__':
    main()
