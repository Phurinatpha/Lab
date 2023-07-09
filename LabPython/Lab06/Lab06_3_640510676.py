#!/usr/bin/env python3
# ชื่อ นามสกุล
# 640510676
# Lab 06
# Problem 3
# 204111 Sec 002

def factorize(num):
    i = 2           
    num0 = num #ค่า num นอก loop ไว้เทียบในกรณีที่ค่านั้นเป็น prime
    print(num,"is " , end="") 
    while ((num**0.5)>=i):  #ทำไปจนกว่า i จะมีค่ามากกว่า รูท num 
        if (num%i==0):      #ถ้าหารแล้วได้ 0 แสดงกว่าตัว i นั้นเป็นตัวประกอบของ num 
            num /= i        #นำ num/i เพื่อไปวนลูป
            print(i,end=" * ") #print i ออกมาตจามด้วย * แต่จะไม่มีตัวท้ายที่เหลทอจากการหาร
        else:               #ถ้าหารไม่ลงตัวให้เพื่มค่าตัวหารไปจนกว่าจะมากกว่า รูทnum
            i += 1
    #if (num == 0 or num==1):
        #print(int(num))
    if (num0 != 0 and num0 == num) and (num0 != 1): #ค่า num เป็น prime อยู่แล้ว
        print("prime")
    else:   #ค่าคัวท้ายของ num 
        print(int(num)) 
        
def main():
    num = int(input())
    factorize(num)

if __name__ == '__main__':
    main()
