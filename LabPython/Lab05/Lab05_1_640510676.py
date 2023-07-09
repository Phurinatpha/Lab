#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 1
# 204111 Sec 002

def euclid_dis(x1, y1, x2, y2): #เป็นการหาระยะทางระหว่างกลางวงกลมที่ 1 กับ 2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def intersects(x1, y1, r1, x2, y2, r2, epsilon=10**-6): #หาว่าวงกลมทั้ง 2 นั้นมีการกระทำเช่นไนต่อกัน
    dis = euclid_dis(x1, y1, x2, y2) #ระยะระหว่าง 2 วงกลม
    if (dis==r1+r2) or abs(dis==r1-r2) or (dis==0 and (r1-r2)==0) or abs(dis-r1-r2)<=epsilon or abs(r1-r2-dis)<=epsilon or (dis==0 and abs(r1-r2)<=epsilon):
        res = 0 	#กรณีสัมผัสกันและมีค่าน้อยกว่า epsilon(นับว่าสัมผัสถ้าระยะของเส้นน้อยกว่า epsilon)
    elif (dis>r1+r2) or (dis==0 and (r1-r2)!=0) or dis<abs(r1-r2): 
        res = -1 	#กรณีไม่สัมผัสกันและไม่แตะกัน
    else: #เคสตัดกัน
        res = 1
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
    print(intersects(x1, y1, r1, x2, y2, r2))

if __name__ == '__main__':
    main()



