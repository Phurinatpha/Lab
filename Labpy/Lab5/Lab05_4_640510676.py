#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 4
# 204111 Sec 002

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    if ((l1>(l2+w2)) or (t1>(t2+h2)) or ((l1+w1)<l2) or (t1+h1<t2)): #เป็นการเปรียบเทียบจุดว่ามีค่ามากกว่ากัน(ระบบพิกัดฉาก)หรือไม่ เช่น l1 มุมซ้ายของ a นั้น> มุมว่าขวาของ b ไหม ถ้าใช่ก็แสดงว่า 4 เหลี่ยมทั้ง 2 ไม่ทับกัน
        return False
    else: #คิดกรณีไม่ทับจะง่ายกว่ากรณีทับ ดังนั้นให้กรณีทับเป็น else
        return True

def main():
    l1 = int(input())
    t1 = int(input())
    w1 = int(input())
    h1 = int(input())
    l2 = int(input())
    t2 = int(input())
    w2 = int(input())
    h2 = int(input())
    print(is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2))


if __name__ == '__main__':
    main()
