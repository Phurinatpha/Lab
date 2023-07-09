#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 1
# 204111 Sec 002


def main():
    print(is_anagram('I am Lord Voldemort!!! ', 'Tom Marvolo Riddle'))

def is_anagram(str1,str2):
    a = ''
    for i in str1:                      #ถ้าอยู่ในระยะของ str1 
        if i.isalpha():                 #ให้เช็คว่าเป็นอักษรไหม ถ้าใช่ นำเข้า str(a)
            a = ''.join([a,i])          
    a = sorted(list(a.casefold()))      #เรียง a-z

    b = ''
    for i in str2:
        if i.isalpha():
            b = ''.join([b,i])
    b = sorted(list(b.casefold()))

    if a == b and len(a) == len(b):     #ถ้าlist เท่ากัน ขนาดต้องเท่ากันและทุกตัวเท่ากัน
        return True                     
    else:                               #ถ้าไม่ก็ส่ง false
        return False


if __name__ == '__main__':
    main()
