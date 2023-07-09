#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 07
# Problem 5
# 204111 Sec 002

import string
def main():
    # x = int(input(""))
    print(num_to_word(1000000))
    print(num_to_word(200000000))
    print(num_to_word(9000000))
    print(num_to_word(1000000000))
    print(num_to_word(9000000000))
    print(num_to_word(10000000000))
    # print(num_to_word(80000000000))
    # print(num_to_word(700000000000))
    # print(num_to_word(1489662012))

def num_to_word(num):
    thousand = 1000
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000
    f_n = []
    list_bank = ''
    if num == 0:
        return 'zero'
    while num > 0: 
        if num>999999999 and num<trillion:
            num1 = num//1000000000
            num = num%1000000000
            f_n = list(three_digits_to_word(num1))
            f_n.append(" billion ")
        elif num>999999 and num<billion:
            num1 = num//1000000
            num = num%1000000
            f_n += list(three_digits_to_word(num1))
            f_n.append(" million ")
        elif num>999 and num<million:
            num1 = num//1000
            num = num%1000
            f_n += list(three_digits_to_word(num1))
            f_n.append(" thousand ")
        elif num>0 and num<thousand:
            num1 = num
            num = 0
            f_n += list(three_digits_to_word(num1))
    for i in f_n:
        list_bank += i
    return list_bank

def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five",
                 "six", "seven", "eight", "nine"]
    tens_ninet = ["ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_list = ["", "", "twenty", "thirty", "forty", "fifty",
                     "sixty", "seventy", "eighty", "ninety"]
    one_h = ""
    ten = ""
    unit = ""
    list_strnum = ""
    for i in range(3):
        if n>99 and n<999:
            ou_o = divmod(n, 100)
            n = ou_o[1]
            one_h = unit_list[ou_o[0]] +" hundred "
        elif n>9 and n<20:
            on_t = divmod(n, 10)
            ten = tens_ninet[on_t[1]]
        elif n>=20 and n<=99:
            ontl = divmod(n, 10)
            n = ontl[1]
            ten = tens_list[ontl[0]]
        else:
            onun = divmod(n ,10)
            unit = unit_list[onun[1]]
    list_allnum =[one_h,'',ten,'',unit]
    if ten!='' and unit!='':
        list_allnum[3] = "-"
    for i in list_allnum:
        list_strnum +=i
    return list_strnum     

if __name__ == '__main__':
    main()
