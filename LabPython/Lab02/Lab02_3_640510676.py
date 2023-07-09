#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 02
# Problem 3
# 204111 Sec 002

print ("First Equation")
m1 =float(input("Input m1: ")) #ค่า m เป็นค่าความชันเป็น float 
b1 =float(input("Input b1: ")) #เป็นค่าคงตัวตามสมการเส้นตรง

print ("Second Equation")
m2 =float(input("Input m2: ")) 
b2 =float(input("Input b2: ")) 

x = -((b1-b2)/(m1-m2)) #หาค่า x ให้ y เป็น 0 ตามหลักการสมการเส้นตรง
y = (m1*x)+b1 #หาค่า y
print ("The point of intersection is at x = %.2f and y = %.2f " %(x,y)) #แสดงค่า x และ y 