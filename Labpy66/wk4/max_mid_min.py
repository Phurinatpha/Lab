def my_min_mid_max(a, b, c):
    maxx = a
    minn = c

    if b > maxx:
        maxx = b
    if c > maxx:
        maxx = c
        minn = b
    if a < minn:
        minn = a
    if c < minn:
        minn = c
    if b < minn:
        minn = b

    print("min =", minn)
    print("mid =", (a+b+c)-maxx-minn)
    print("max =", maxx)

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_min_mid_max(a, b, c)

if __name__ == '__main__':
    main()