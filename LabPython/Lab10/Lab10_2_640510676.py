#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 2
# 204111 Sec 002

def is_palindrome(x, b):
    res = []
    while x!=0: #เป็นการแปลงฐานจากฐาน 10 เป็นฐาน b
        remi = x%b  
        res.append(remi)
        x = x//b
    rev = list(reversed(res)) #ตัวแปรใหม่จากการ rev ตัวเดิม

    if res == rev: #ถ้ารีแล้วเท่ากันก็เป็น palindrome
        return True
    else:
        return False

def main():
    x = int(input())
    b = int(input())
    print(is_palindrome(x, b))

if __name__ == '__main__':
    main()

