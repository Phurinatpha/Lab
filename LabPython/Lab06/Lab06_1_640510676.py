#!/usr/bin/env python3
# ภูริณัฐ  ภาณุพงศ์สกุล
# 640510676
# Lab 06
# Problem 1
# 204111 Sec 002

def int_power(x, y):
    num = 1 #ให้ค่าตัวแปรเป็น 1 ใช้คำควณ -y
    if (y>0): #กรณีที่เป็น +
        for function in range(y): #ทำลูปไปจนกว่าค่า y จะครบ
            num = num*x 
    else: #กรณีที่เป็น -
        num=1.0
        for function in range(-y): #ค่า -y ทำให้ลูปต้องลดไปที่ละค่า
            num = num/x

    return num


def main():
    x = float(input())
    y = int(input())
    print("{:.6f}".format(int_power(x,y)))
    
if __name__ == '__main__':
    main()
