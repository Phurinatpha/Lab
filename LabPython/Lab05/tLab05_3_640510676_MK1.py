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
    delta = date1 - date2   #คำนวณวันโดยการนำวันสงกรานต์เป็นตัวตั้ง(ใช้ import date ข่วย)

    if (date2>date1): #กรณีที่วัน input มากกว่า(เกิน) วันสงกรานต์
        y=y+1 #จะผ่านไป 1 ปีจึงนำ y+1 
        if ((y%4==0 and y%100!=0) or y%400==0): #แล้วนำมาเช็คว่าปัที่ +1 นั้นเป็น leaf year หรือไม่
            dayleft = 366+delta.days #ค่าที่ได้จะเป็นลยจริงนำมาบวก 366
        else: #หากไม่ใช่ให้นำจำนวนวันมาบวก 365
            dayleft = 365+delta.days
    else: #กรณี input ก่อนวันสงกรานต์
        dayleft = delta.days  #แสดงจำนวนวันจาก import date ได้เลย

    return dayleft
def main():
    d = int(input())
    m = int(input())
    y = int(input())
    print(count_down_to_songkran(d, m, y))


if __name__ == '__main__':
    main()
