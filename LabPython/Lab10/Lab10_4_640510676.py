#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 2
# 204111 Sec 002

def uniform(line):
    c_up = 0
    c_lo = 0
    for i in line: #ลูปเช็คตัวเล็ก-ใหญ่ 
        if i.isupper():
            c_up += 1
        elif i.islower():
            c_lo += 1
    
    if c_up > c_lo: #ถ้าพิมพ์ใหญ่เยอะกว่าให้เป็นตัวใหญ่หมด
        line = line.upper()

    elif c_up < c_lo: #ถ้าพิมพ์เล็กเยอะกว่าก็ให้เป็นเป็นพิมพ์เล็กหมด
        line = line.lower()

    elif line[0].isupper(): #ถ้าเท่ากันแล้วตัวแรกเป็นพิมพ์ใหญ่ก็ให้เป็นพิมพ์ใหญ่หมด
        line = line.upper()

    else:
        line = line.lower() #ถ้าเท่ากันแล้วตัวแรกเป็นพิมพ์เล็กก็ให้เป็นพิมพ์เล็กหมด

    return line

def main():
    line = str(input())
    print(uniform(line))

if __name__ == '__main__':
    main()

