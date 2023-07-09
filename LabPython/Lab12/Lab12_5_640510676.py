#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 12
# Problem 5
# 204111 Sec 002

def reverse_num(num, ps=0):
    if num < 10:
        return ps + num
    ps = ps * 10 + num%10 * 10
    return reverse_num(num // 10, ps)

def main():
    print(reverse_num(1234))

if __name__ == '__main__':
    main()

#work with stackoverflow(litle bit)
