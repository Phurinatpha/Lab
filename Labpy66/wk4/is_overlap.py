def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    return not ((l1 > (l2 + w2)) or (t1 > (t2 + h2)) or ((l1 + w1) < l2) or (t1 + h1 < t2))


def main():
    print(is_overlapped(10, 10, 100, 150, 50, 100, 150, 200))


if __name__ == '__main__':
    main()