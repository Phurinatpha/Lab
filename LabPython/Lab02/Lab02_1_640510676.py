#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 02
# Problem 1
# 204111 Sec 002

f = int(input("Input temperature in Fahrenheit: ")) #รับค่า f เป็น int เพื่อนำไปคำนวณใน c เพื่อให้ได้ค่า c ที่เป็นองศาเชียลเซียส
c = ((f-32)/9)*5 #สุตรการคำนวณหา c 
print ("%.2f degree Fahrenheit is %.2f degree Celsius" %(f,c)) #เป็นการแสดงค่า f,C
