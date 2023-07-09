#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 3
# 204111 Sec 002

def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def coprime_factor(a, b):
    a = prime_factor(a)
    b = prime_factor(b)
    co = []     
    for i in b:  #เช็คว่าตัวนั้นอยู่ในอีก list รึเปล่าถ้าแม่นก็ให้เพิ่มไปใน list co แล้วลบ a ออกเพื่อไม่ให้เช็ค ซ้ำ
        if i in a:
            co.append(i)
            a.remove(i)
        else:
            pass
    return co

def main():
    a = 9978320
    b = 62244
    print(prime_factor(a))
    print(prime_factor(b))
    print(coprime_factor(a, b))


if __name__ == '__main__':
    main()

#co-work 640510625