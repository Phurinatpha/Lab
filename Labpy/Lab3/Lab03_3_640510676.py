#!/usr/bin/env python3
# ภูริณัฐ  ภาณุพงศ์สกุุล
# 640510676
# Lab 03
# Problem 3
# 204111 Sec 002

import math

def octagon_area(x): #หาพื้นที่จากการคิดพื้นที่สีเหลี่ยมผืนผ้า- 4*(พท.สามเหลี่ยม)(มีสามเหลี่ยมอยู่ 4 รูป)
    # เขียนโค้ดเพิ่มตรงนี้นะจ๊ะ
    tri = (4*(1/2*(x/3)*(x/3)))  #พท.สามเหลี่ยม 4 รูป
    area = x*x                   #พท.4เหลี่ยม
    octa = area-tri              #พท.8เหลี่ยมจาก (พท.4เหลี่ยม- พท.สามเหลี่ยม 4 รูป)
    return octa                 #ส่งค่า พท.8 เหลี่ยม

def main():
    # รับด้านจาก user
    x = float(input())
    # พิมพ์พื้นที่ของรูปแปดเหลี่ยมด้านเท่า
    print(octagon_area(x))

if __name__ == '__main__':
    main()
