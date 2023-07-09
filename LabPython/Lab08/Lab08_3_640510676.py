#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 3
# 204111 Sec 002

def main():
    nums = [1,2,3,4]
    n = 1
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))   #[4, 1, 2, 3]

    n = 105
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[4, 1, 2, 3]

    n = -1
    print(nums)  #[1, 2, 3, 4]
    print(nondest_rotate_list(nums, n))  #[2, 3, 4, 1]

def nondest_rotate_list(list_a, n):
    n_n = abs(n)%len(list_a)
    if n>0:
        list_a =  list_a[-n_n:] + list_a[:-n_n] #pos-case ให้sliing เอาด้านหลัง + ด้านหน้า
    else:
        list_a = list_a[n_n:] + list_a[:n_n] # ด้านหน้า + ด้านหลัง
    return list_a

if __name__ == '__main__':
    main()