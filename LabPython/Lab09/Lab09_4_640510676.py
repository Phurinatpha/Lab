#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 4
# 204111 Sec 002

def main():
    list_a = [1, 2, [[2, [[145], 34]], [48, 22]]] 
    print(sum_nested_list(list_a))

def sum_nested_list(list_a):
    total = 0
    for i in list_a: 
        if isinstance(i, list): #เช็คว่าเป็น list ไหมถ้าเป็นให้วนใน function อีกรอบแล้วแล้ว + เข้าผลรวม
            total += sum_nested_list(i)
        else:
            total += i #ไม่เป็นก็บวกไปเลยยยย
            
    return total



if __name__ == '__main__':
    main()

