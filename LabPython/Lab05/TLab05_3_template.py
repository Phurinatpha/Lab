#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 3
# 204111 Sec 002

def count_down_to_songkran(d, m, y):
    from datetime import date 
    date1 = date(y, 4, 13) 
    date2 = date(y, m, d)
    delta = date1 - date2

    if (date2>date1):
        y=y+1
        if ((y%4==0 and y%100!=0) or y%400==0):
            d = d+1
            dayleft = 366+delta.days
        else:
            dayleft = 365+delta.days
    elif (date1>=date2):
        dayleft = delta.days
    else:
        pass

    return dayleft
def main():
    d = int(input())
    m = int(input())
    y = int(input())
    print(count_down_to_songkran(d, m, y))


if __name__ == '__main__':
    main()
