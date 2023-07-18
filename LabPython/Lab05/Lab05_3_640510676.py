#!/usr/bin/env python3

# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 3
# 204111 Sec 002

from datetime import date #เรียกใช้การทำงานของ date 
def count_down_to_songkran(d, m, y):
    date1 = date(y, 4, 13)  #ให้วันสงกรานต์เป็นตัวตั้งหรือมาร์คในการหาจำนวนวัน
    date2 = date(y, m, d)   #วันที่รับเข้า input 
    if (date2>date1): #กรณีที่วัน input มากกว่า(เกิน) วันสงกรานต์
        date1 = date((y+1), 4, 13) #เกินปีเอา y+1 
        delta = date1 - date2   #คำนวณวันโดยการนำวันสงกรานต์เป็นตัวตั้ง(ใช้ import date ข่วย)
    else: #กรณี input ก่อนวันสงกรานต์
        delta = date1 - date2   #แสดงจำนวนวันจาก import date ได้เลย
        
    return delta.days
def main():
    d = int(input())
    m = int(input())
    y = int(input())
    print(count_down_to_songkran(d, m, y))


if __name__ == '__main__':
    main()
