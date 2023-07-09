#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 02
# Problem 2
# 204111 Sec 002

h =float(input("Input height (m): ")) #รับค่าความสูงเป็น float เพราะส่วนสูงมีหน่วยเป็น m 
w =float(input("Input weight (kg): ")) #รับค่าน้ำหนักเป็น float เพราะอาจจะมีน้ำหนักเป็นจุดทศนิยม
bmi =(w/(h**2)) #สูตรคำนวณค่า bmi
print ("BMI is %.4f " %bmi) #แสดงค่า bmi เป็นทศนิยม 4 ตำแหน่ง