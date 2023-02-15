#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 1
# 204111 Sec 002

def love6(first, second):
    #each of them is 6
    if (first==6) or (second==6): #เงื่อนไขที่ 1 ตัวแรกหรือตัวที่ 2 เป็น 6 ให้ส่งค่าคววามจริงเป็น จริง
        return True
    # sum of two is 6
    elif ((first+second)==6): #เงื่อนไขที่ 2 ผลรวมเป็น 6 แสดงค่าความจริงเป็นจริง
        return True
    # diff of two is 6
    elif ((abs(first-second))==6): #เงื่อนที่ 3 ผลต่างเป็น 6 ให้แสดงค่าความจริงเป็นจริง (abs ใส่เพื่อป้องกันผลต่างเป็น -)
        return True
    else: #นอกนั้นให้เป็นค่า เท็๋จ
        return False

def main():
    # receive input from user
    first = int(input())
    second = int(input())
    # print result from function
    print(love6(first,second))

if __name__ == '__main__':
    main()
