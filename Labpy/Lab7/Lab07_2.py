#!/usr/bin/env python3
#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 6XXXXXXXX
# Lab07_2
# 204111 Sec 00?

T3 = '''*
*.*
* * *
'''

T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''


def main():
    n = int(input())
    print(triangle(n), end='')
    test_triangle()

def triangle(n,row = 0):
    if row == 0:
        str = "*\n"
        return str + triangle(n,row+1)
    elif row < n-1:
        str = "*" + ("." * (2*row-1)) + "*\n"
        return str + triangle(n,row+1)
    else:
        return ("* " * (n-1)) + "*\n"

def test_triangle():
    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")


if __name__ == '__main__':
    main()
