#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 1
# 204111 Sec 002


def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6): #หาว่าวงกลมทั้ง 2 นั้นมีการกระทำเช่นไนต่อกัน
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    #ระยะระหว่าง 2 วงกลม
    if (dis-(r1+r2)==0) or abs((r1+r2)-dis)<=epsilon:
        res = 0 	#กรณีสัมผัสกันและมีค่าน้อยกว่า epsilon(นับว่าสัมผัสถ้าระยะของเส้นน้อยกว่า epsilon)
    elif (dis<r1+r2):
        res = 1
    else :
        res = -1
    return res

def main():
    # receive input from user
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    # print result from function
    print(circle_intersect(x1, y1, r1, x2, y2, r2))

if __name__ == '__main__':
    main()



