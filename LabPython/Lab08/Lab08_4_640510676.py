#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 2
# 204111 Sec 002

def main():

    n = 1
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]

    n = -1
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[2, 3, 4, 1]

    n = 105
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]

def dest_rotate_list(list_a, n):
    for i in range(abs(n)):
        if n>0:
            p_num = list_a.pop()                    #ใช้  pop เอาตัวท้ายออก
            list_a.insert(0 , p_num)                #แทรก ตน. ที่ต้องการ
        else:
            p_num = list_a.pop(0)
            list_a.insert(len(list_a) , p_num)

if __name__ == '__main__':
    main()