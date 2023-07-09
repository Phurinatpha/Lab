#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 1
# 204111 Sec 002

def square_frame(n, sep=' '): 
    listOn = [[0 for x in range(n)] for y in range(n)] #สร้าง list 2d ขนาด n*n
    m = 1
    lw = 0
    hi = n-1
    count = int((n+1)/2)  # จน รอบการทำซ้ำ
    
    for i in range(count):
        for j in range(lw,hi+1):  #แถวบนสุด และ แถวต่อมาโดยที่จะมีขอบด้านของข้างเป็น 0 ([0,7,8,9,0])
            if m <= 9:
                listOn[i][j] = ''.join('0'+str(m))
            else:
                listOn[i][j] = m
            m = m+1
        for j in range(lw+1, hi+1): # col ขวาสุดทำจาก i+1 โดยจะปริ้นหลักก่อนแต่จะมีขอบ 0
            if m <= 9:    
                listOn[j][hi] = ''.join('0'+str(m))
            else: 
                listOn[j][hi] = m
            m = m+1
        for j in range(hi-1,lw-1,-1): #ปริ้นแถวล่างแบบย้อนจากหลังมาด้าน
            if m <= 9:    
                listOn[hi][j] = ''.join('0'+str(m))
            else: 
                listOn[hi][j] = m
            m = m+1
        for j in range(hi-1,lw,-1): #ปริ้นจากล่างขึ้นบน
            if m <= 9:    
                listOn[j][lw] = ''.join('0'+str(m))
            else: 
                listOn[j][lw] = m
            m =m+1

        lw = lw + 1
        hi = hi - 1 

    res = (n*n) - ((n-2) * (n-2)) #ตัวสุดท้ายที่ของวงนอกจะมีค่า = res
    for i in range(n):
        for j in range(n):
            if int(listOn[i][j]) <= res: #ถ้าค่าใน list 2d นั้นน้อยกว่า res ให้ไปเช็คว่าเป็นหลักสุดรึป่าวถ้าไม่ใช่ก็ให้ปริ้น sep ไปด้วย
                if j < n-1:
                    print(listOn[i][j], end=sep)
                else:
                    print(listOn[i][j], end="")  #หลักสุดท้ายต้องไม่ปริ้น sep เดะเกิน
            else:
                print(sep*2, end=sep) #ถ้าเป็นตรงกลางให้ปริ้น sep เยอะๆเดียวไม่พอ
        print() 

def main():
    n = int(input())
    square_frame(n, sep='.')

if __name__ == '__main__':
    main()

