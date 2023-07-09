#!/usr/bin/env python3
# ภูริณัฐ  ภาณุพงศ์สกุล
# 640510676
# Lab 03
# Problem 1
# 204111 Sec 002

import math

def main():
   # รับข้อมูลพื้นที่ผิวจาก user
   surface_area = float(input("input surface area: "))
   # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
   radius = find_r_from_surface_area(surface_area) #func ที่เขียน(copy elab)
   # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
   volume = sphere_volume(radius) # ใช้ตัวแปล voloume มาแสดงค่า func. sphere_voloume(redius)
   # แสดงปริมาตรทรงกลม
   print("volume = {0:.2f}".format(volume))  #แสดงค่าออกมาเป็นทศนิยม 2 ตัวแหน่ง


def find_r_from_surface_area(surface_area):
    # เขียนโค้ดเพิ่มตรงนี้
    return math.sqrt(surface_area/(4*math.pi)) #ส่งค่า r หาสูตรได้จากการย้ายข้างหา r


def sphere_volume(radius):
    # เขียนโค้ดเพิ่มตรงนี้
    return 4/3*math.pi*radius**3 #ส่งค่าสูตรปริมาตรทรงกลม


if __name__ == '__main__':
    main()

