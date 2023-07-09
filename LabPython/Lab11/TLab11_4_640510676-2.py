#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 4
# 204111 Sec 002

def polynomial_addition(p1, p2):
    p_1 = list(reversed(sorted(p1)))
    p_2 = list(reversed(sorted(p2)))
    maxx = max(len(p_1),len(p_2))
    zipp1 = list(zip(*p_1))
    zipp2 = list(zip(*p_2))
    if zipp1 == [] or zipp2 == []:
        if zipp1 == []:
            return p_2
        else:
            return p_1

    for i in range(maxx-1,0,-1):
        if len(p_1) != len(p_2):
            if p_1[i][0] not in zipp2[0]:
                p_2.append((i,0))
                p_2.sort()
                p_2.reverse()
            elif p_2[i][0] not in zipp1[0]:
                p_1.append((i,0))
                p_1.sort()
                p_1.reverse() 

    print(p_1)
    print(p_2)
    lf = []
    lb = []
    for i in range(len(p1)):
        pb = p_1[i][1] + p_2[i][1]
        lb.append(pb)
        pf = p_1[i][0]
        lf.append(pf)

    zipp = list(zip(lf,lb))
    zippp = []
    for i in zipp:
        if i[1] != 0:
            zippp.append(i)

    return zippp

def main():
    p1 = [(2, 2), (0, 1)]
    p2 = [(0, 1)]
    print(polynomial_addition(p1, p2))

if __name__ == '__main__':
    main()

