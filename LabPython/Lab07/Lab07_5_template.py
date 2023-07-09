#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 06
# Problem 1
# 204111 Sec ???

def main():
    num = int(input("num: "))
    pos = int(input("pos: "))
    result = rotate(num, pos)
    print(type(result))
    print(result)

def rotate(num, pos):
    max_dg = len(list(str(num)))
    if pos>0:
        for i in range(pos):
            num = (num%10*10**(max_dg-1)) + (num//10)
    else:
        for i in range(abs(pos)):
            num = ((num%10**(max_dg-1))*10) + (num//10**(max_dg-1))
    return num


if __name__ == '__main__':
    main()
