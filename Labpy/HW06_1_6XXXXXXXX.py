#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 6XXXXXXXX
# HW06_1
# 204111 Sec 00?

from math import isclose


def main():
    #print(test_pi())
    print(pi(1))
    #pass

def pi(n):
    if n==0:
        return 3
    else:
        return pi(n-1) + ((-1)**(n-1))*(4/((2*n)*(2*n+1)*(2*n+2)))


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    main()
