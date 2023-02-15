#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 4
# 204111 Sec 002

def round_to_int(x):
    # WRITE YOUR CODE HERE
    
    if (x>=0):  #plus case
        int_num = (x*10)%10 #หาตัวท้ายเพื่อไปเช็คในเงื่อนไขว่ามากกว่าหรือเท่ากับ 5 ไหมถ้าใช่ให้นำเอา x+1 หากไม่คืนค่า x 
        if (int_num>=5):
            x = (x+1)
        else:
            x = (x)
    else:   #minus case
        miint_num = (abs(x)*10)%10 #หาตัวท้าย(ที่เป็นลบ) เพื่อไปเช็คในเงื่อนไขว่ามากกว่าหรือเท่ากับ 5 ไหมถ้าใช่ให้นำเอา x-1 หากไม่คืนค่า x 
        if (miint_num>=5):
            x = (x-1)
        else:
            x = (x)
    return int(x) #ให้คืนค่าเป็น int เพื่อให้เป็น จน.เต็ม


def main():
    # receive input from user
    x = float(input())
    # print result from function
    print(round_to_int(x))

if __name__ == '__main__':
    main()
