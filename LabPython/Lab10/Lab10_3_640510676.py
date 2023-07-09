#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 3
# 204111 Sec 002

def patterned_message(message, pattern):
    out = [' ']*len(pattern)
    n=0
    message = ''.join((message.split())) 
    lenm = len(message)
    pat = list(enumerate(pattern)) #การสร้าง list ของ Tuple โดยใน Tuple จะประกอบตัว index,value จากจำนวนของ pattren
    print(pat)
    if pat[0][1]== "\n":  #ลบ \n ถ้าตัวแรกเป็น \n 
        del pat[0]

    for i in range(len(pat)): #ลูปเช็คค่าว่าเป็น * ไหมถ้าเป็นก็แทนค่าไปตามค่า n%lenm 
        if '*' in pat[i][1]:
            out[i] = message[n%lenm]
            n+=1
        elif '\n' in pat[i][1]: #ถ้าเป็น \n ให้ขึ้นบรรทัดใหม่
            out[i] = '\n'

    outp = ''.join(out) 
    print(outp)

def main():
    patterned_message("Three Diamonds!",'''
   *     *     *
  ***   ***   ***
 ***** ***** *****
  ***   ***   ***
   *     *     *
''')


if __name__ == '__main__':
    main()

