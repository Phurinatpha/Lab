#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 2
# 204111 Sec 002

#def my_max_mid_min(x, y, z):
    # WRITE YOUR CODE HERE
    #case 1 a b c ไม่ซ้ำกันมี 6 วิธี


def is_p_triple(x, y, z):
    if (x>y>z):
        maxx = x
        midd = y
        minn = z
    elif (x>z>y):
        maxx = x
        midd = z
        minn = y
    elif (y>x>z):
        maxx = y
        midd = x
        minn = z
    elif (y>z>x):
        maxx = y
        midd = z
        minn = x
    elif (z>x>y):
        maxx = z
        midd = x
        minn = y
    elif (z>y>x):
        maxx = z
        midd = y
        minn = x

    #case 2 a b c มี 2 ตัวซ้ำกัน และ ตัวซ้ำมีค่ามากกว่าอีกตัวที่ต่าง มี 3 วิธี
    elif ((x==y) and x>z and y>z):
        maxx = x
        midd = y
        minn = z
    elif ((y==z) and y>x and z>x):
        maxx = y
        midd = z
        minn = x
    elif ((x==z) and x>y and z>y):
        maxx = x
        midd = z
        minn = y

    #case 3 a b c มี 2 ตัวซ้ำกัน และ ตัวซ้ำมีค่าน้อยกว่าอีกตัวที่ต่าง มี 3 วิธี
    elif ((x==y) and x<z and y<z):
        maxx = z
        midd = x
        minn = y
    elif ((y==z) and z<x and y<x):
        maxx = x
        midd = y
        minn = z
    elif ((x==z) and x<y and z<y):
        maxx = y
        midd = z
        minn = x

    #case 4 a b c ซ้ำกันทั้ง 3 ตัว
    else:
        maxx = x
        midd = y
        minn = z
    
    if ((maxx**2) == (midd**2) + (minn**2)):
        return True
    else:
        return False
    
def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(is_p_triple(x, y, z))

if __name__ == '__main__':
    main()
