#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 2
# 204111 Sec 002


def classify(list_x):
    list_a = []
    list_b = []
    list_c = []

 #เขียนโค้ดลงไปตรงนี้
    for i in range(len(list_x)):                    
        if isinstance(list_x[i], int):              #ให้เช็คว่า list_x ตัวที่ i เป็น int ไหม ถ้าใช่ก็เป็น int 
            list_a.append(list_x[i])                
        elif isinstance(list_x[i], float):          #เช็คให้เป็น float 
            list_b.append(list_x[i])                
        else:
            list_c.append(list_x[i])                #อันอื่นเป็น str
#ในpython เราสามารถ return ได้มากกว่า 1 ค่า โดยผลลัพธ์จะถูกมัดรวมออกไปเป็นค่าเดียวซึ่งมี type เป็น  Tuple
    return list_a, list_b, list_c

def main():
    x = [8, 179, "LZCeKxyIX0'", 74, "DMQyEVPOW0'", 6.53, "v0'EBTMghRI", 608, -72, 744, -284.815]
    list_x = x
    list_int, list_float, list_string = classify(x)
    print(type(list_int), list_int)
    print(type(list_float), list_float)
    print(type(list_string), list_string)



#<class 'list'> [10, 4]
#<class 'list'> [23.5]
#<class 'list'> ['he4>lo']


if __name__ == '__main__':
    main()
