#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 2
# 204111 Sec 002

def search_event(list_x, key):
    key = key.split("/") #แปลง key จาก 01/01/1010 เป็น 1/1/1010
    if key[0][0] == '0':
        key[0] = key[0][1]
    if key[1][0] == '0':
        key[1] = key[1][1]

    key = '/'.join(key)
    for i in range(len(list_x)): #ถ้าตัวใน list_x ตรงคีย์ ก็ให้ re เป็น list ตำแหน่งนั้น
        if list_x[i][0] == key:
            re = list_x[i]
            break
        else:
            re = None
    return re

def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
 ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
 ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
 ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
 ("9/11/2042", "Event I")]
    event = search_event(list_x, "29/02/2032")
    print("---")
    print(event)



if __name__ == '__main__':
    main()

