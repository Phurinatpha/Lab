#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 03
# Problem 5
# 204111 Sec 002

import math
def main():
    # รับตัวเลขจาก user
    number = int(input('Input number: ')) 
    k = int(input('Input digit: '))
    value = int(input('Input digit: '))
    # พิมพ์ตัวเลขหลังจากการเปลี่ยนค่าหลักที่กำหนด
    print(set_kth_digit(number, k, value))

def kth_digit(number, k): #func.หาตำแหน่งที่จะนำมาเปลี่ยนค่า
    # Copy มาจากข้อ 4 ได้เลย
    kth = ((abs(number)//(10**k))%10)
    return kth

def set_kth_digit(number, k, value): #เป็น func ที่ใช้ในการเปลี่ยนค่าหลัก k ด้วย value
    # เขียนโค้ดเพิ่มเอง ใช้ฟังก์ชัน kth_digit ช่วยได้นะ
    Number = number-(kth_digit(number, k)*10**k) + (value*10**k)
    #นำค่าที่หาได้จาก func. kth_digit(number, k) ลบด้วยค่าที่จะเปลี่ยนยกกำลังด้วย 10**kเพื่อให้ได้หลักที่ต้องการ
    return Number
    #นำ number ลบด้วย setdigit จะได้ค่าที่ต้องการจะเปลี่ยนในหลัก k ที่มีตัวเลข 0-9 ทำให้นำมาลบแล้วจะได้ค่าที่ต้องการเปลี่ยน

if __name__ == '__main__':
    main()
