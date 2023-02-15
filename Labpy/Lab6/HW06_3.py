#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 6XXXXXXXX
# HW06_1
# 204111 Sec 00?



def main():
    #print(test_pi())
    print(left_max2([2,5,2,5,2,5,5]))
    #pass

def left_max2(list_n,ma=0,i=0):
    if len(list_n) == i:
        list_a = list_n
        return list_a
    else:
        ma = max(list_n[i],ma)
        list_n[i] = ma
        return left_max2(list_n,ma,i+1)

# def left_max(n):
#     if n<10:
#         return n
#     else:
#         max_cur = left_max(n//10) 
#         return max_cur*10 + max(n%10,max_cur%10)


if __name__ == '__main__':
    main()

