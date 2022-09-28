#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 5
# 204111 Sec 002

def zodiac_element(year):
    if year%2 ==0:
        yy = "Yang"
    else:
        yy = "Yin"

    y_zo = abs((year)%12) #ปี input ลบด้วยปีที่ตั้งไว้ในที่นี้ใช้ปี 1996 เป็นปีตั้งเพื่อให้ปีหนูเป็นปีแรกของ zodiac แล้วนำมา %12 เพื่อให้ได้ค่าที่ไม่เกิน 12 (com นับปีที่ 1 เป็น 0)
    zodiac = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"] #ใช้ array มาช่วยในการเก็บค่า zodiac
    
    y_ele = abs((year+6)%10//2) #หาธาตุจากการนำปีมา +6 (เราอยากได้เลข 0-4)แล้ว %10 ให้ได้ 10 ค่าจึงนำมาหาร 2 ให้เหลือ 5 ค่า(0-4)
    element = ["Wood", "Fire", "Earth", "Metal", "Water"]

    return ('{0} {2} {1}'.format(yy,zodiac[y_zo],element[y_ele])) #แสดงค่าโดยใช้ array มาเรียกค่า zodiac ต่างๆ และ element

def main():
    year = int(input())
    print(zodiac_element(year))


if __name__ == '__main__':
    main()

	



