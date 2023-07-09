#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 5
# 204111 Sec 002

def radix_int(list_x):
    return list_x.sort() 

def main():
    list_x = [19, 48, 175, 290, 873, 7, 43, 69]
    radix_int(list_x)
    print('--------') 
    print(list_x)

if __name__ == '__main__':
    main()

