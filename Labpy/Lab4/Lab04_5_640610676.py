#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 5
# 204111 Sec 002

def nearest_odd(x):
    # WRITE YOUR CODE HERE
    x = (x*10)//10  #ใช้เป็นสูตรการคำนวณเพื่อให้ได้ค่าแบบไม่เอาเศษ
    if (x%2 == 0): #ถ้า x%2เท่ากับ 0(%2 ลงตัวเป็นเลขคู่) ให้ x+1 ให้ได้เป็น จน.คี่
        x = (x+1)
    else:
        x = x     
    return int(x) #แสดงค่า x เป็น จน.เต็ม

def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(nearest_odd(x))

if __name__ == '__main__':
    main()
 