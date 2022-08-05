#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 2
# 204111 Sec 002

def my_max_mid_min(a, b, c):
    # WRITE YOUR CODE HERE
    #case 1 a b c ไม่ซ้ำกันมี 6 วิธี
    if (a>b>c):
        maxx = a
        midd = b
        minn = c
    elif (a>c>b):
        maxx = a
        midd = c
        minn = b
    elif (b>a>c):
        maxx = b
        midd = a
        minn = c
    elif (b>c>a):
        maxx = b
        midd = c
        minn = a
    elif (c>a>b):
        maxx = c
        midd = a
        minn = b
    elif (c>b>a):
        maxx = c
        midd = b
        minn = a

    #case 2 a b c มี 2 ตัวซ้ำกัน และ ตัวซ้ำมีค่ามากกว่าอีกตัวที่ต่าง มี 3 วิธี
    elif ((a==b) and a>c and b>c):
        maxx = a
        midd = b
        minn = c
    elif ((b==c) and b>a and c>a):
        maxx = b
        midd = c
        minn = a
    elif ((a==c) and a>b and c>b):
        maxx = a
        midd = c
        minn = b

    #case 3 a b c มี 2 ตัวซ้ำกัน และ ตัวซ้ำมีค่าน้อยกว่าอีกตัวที่ต่าง มี 3 วิธี
    elif ((a==b) and a<c and b<c):
        maxx = c
        midd = a
        minn = b
    elif ((b==c) and c<a and b<a):
        maxx = a
        midd = b
        minn = c
    elif ((a==c) and a<b and c<b):
        maxx = b
        midd = c
        minn = a

    #case 4 a b c ซ้ำกันทั้ง 3 ตัว
    else:
        maxx = a
        midd = b
        minn = c

    print("max =",maxx)
    print('mid =',midd)
    print("min =",minn)
            

def main():
    # receive input from user
    a = int(input())
    b = int(input())
    c = int(input())
    # call function
    my_max_mid_min(a, b, c)

if __name__ == '__main__':
    main()
