#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 5
# 204111 Sec 002

def main():
    num = int(input("num: "))
    pos = int(input("pos: "))
    result = rotate(num, pos)
    print(type(result))
    print(result)

def rotate(num, pos):
    max_dg = len(str(num))          #หา จน หลัก
    for i in range(abs(pos)):       #ลูปตามต่ำแหน่งที่ต้องการ
        if pos>0:   #ในกรณีที่ค่าต่ำแหน่งมากกว่า 0 ให้นำเอาตัวท้ายที่เกิดจาการ % ไปยกกำลังหลักแล้ว + กับค่าที่ตัดท่ายออก
            num = (num%10*10**(max_dg-1)) + (num//10) 
        else:       #กรณีอื่น(เคส pos-) % เอาตัวแรกออก(ได้ตัวที่เหลือ) แล้ว + ด้วย // ที่ไม่เอาเศษ(จะได้ตัวแรกแทน)
            num = ((num%10**(max_dg-1))*10) + (num//10**(max_dg-1)) 
    return num      #เอาค่า num ออกมาาาาาาาาา(สักที)   

if __name__ == '__main__':
    main()
