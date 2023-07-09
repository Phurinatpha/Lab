#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 2
# 204111 Sec 002

import math
def digit_count(x, base=10):
    x = (math.log(abs(x), base))        #หาจำนวนหลักได้จาก log 
    almost = 10**-6                     
    if (x%1 == 0):                      #ค่า log บางค่าจะไม่ครบหลัก
        x += 1                          #กรณีที่ลงท้ายด่วย .0 จะปัดด้วยการให้เป็นค่าขอบบนไม่ได้(ceil)                          
    elif (1-(float(x)-int(x))<=almost): #กรณีที่ตัวเลขนั้นใกล้จะถึงแต่ไม่ถึง 19.99999999999996 ปัดแล้วตัวเลขไม่ตรง
        x += 1 
    else:                               #กรณีอื่นๆ (เคสที่ไม่ปัญหา)
        x = x
    return math.ceil(x)                 #return โดยการปัดค่า x ให้เป็นขอบบน(ปัดขึ้นหมด)

def main():
    x = int(input("number: "))
    base = int(input("base: "))
    if base ==10:
        print(digit_count(x))
    else:
        print(digit_count(x,base))

if __name__ == '__main__':
    main()




