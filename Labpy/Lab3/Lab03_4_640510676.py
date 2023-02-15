#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 03
# Problem 4
# 204111 Sec 002

import math
def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) #รับค่าตัวเลขเข้ามา
    k = int(input('Input digit: ')) #รับค่าหลักที่ต้องการแสดง
    # พิมพ์ตัวเลขตำแหน่งที่ k ของข้อมูลเข้า
    print(kth_digit(number,k)) #แสดงผล func.kth_digit(number,k)

def kth_digit(number,k): 
    # เขียนโค้ดเพิ่มตรงนี้นะจ๊ะ
    kth = ((abs(number)//(10**k))%10) #(นำ number//หลักที่จะหาจาก(10**k))%10 เพื่อหารเอาเศษ
    return kth

if __name__ == '__main__':
    main()
