#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 06
# Problem 5
# 204111 Sec 002


def longest_digit_run(n): 
    max_re = 1              #ค่าสูงสุดของตัวที่ติดกัน
    re  = 1                 #ค่า จน ที่ติดกันไว้เทียบกับ max_re
    n0 = n%10               #ตัวที่เอามาเทียบ
    n = n//10               #ตัวเหลือ
    count = n0              #เทียบว่าเดิม(re)กับค่าใหม่ == กันรึเปล่า
    while (n != 0):         #ทำไปจนกว่าค่า n = 0
        n0 = n%10           #ค่า n0 จากการ loop
        n = n//10           #ค่า n จาก loop
        if (count == n0):   #รอบแรกจะดึงเอาค่า count มาเทียบกับค่า n0 ใน loop 
            re = re + 1     #ถ้าเท่ากันค่า re + 1 
        else:               #ถ้าไม่เข้า if ก็ให้ จน ที่ติดกัน = 1 แล้วให้ค่า count = n0 ที่ผ่านการตัดตัวล่าสุดออก(เปลี่ยน)
            re = 1          
            count = n0
        if (re > max_re):   #ถ้า re>max_re ให้ค่า max ใหม่ = re
            max_re = re
    return max_re
    
def main():
    n = int(input())
    print(longest_digit_run(n))

if __name__ == '__main__':
    main()
