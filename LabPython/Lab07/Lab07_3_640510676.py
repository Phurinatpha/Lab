#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 3
# 204111 Sec 002

def main():                     
    n = int(input())
    triangle(n)

def triangle(n):                            
    for i in range(n):                      #แถว i 
        for j in range(i+1):                #หลัก j 
            if j==0 and i<n-1 and i>0:      #ถ้าหลักแรกเป็น 0 และ แถวต้องเป็นแถวที่ 2 แต่ไม่เกินแถวรองสุดท้ายให้ ปริ้น * จบด้วย .
             print('*',end='.')
            elif j==0 or i==j or i==n-1:    #กรณีที่เป็นหลักแรก หรือเป็นสันของสามเหลี่ยม หรือเป็นแถวสุดท้ายให้ปริ้น * แล้วตามด้วยช่องว่าง
                print('*',end=' ')
            else:                           #อื่นๆให้ปริ้น ..
                print('.', end='.')
        print("")                           #ใช้ขึ้นบรรทัดใหม่
 


if __name__ == '__main__':
    main()

