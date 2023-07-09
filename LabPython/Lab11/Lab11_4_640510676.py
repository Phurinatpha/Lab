#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 4
# 204111 Sec 002

def polynomial_addition(p1, p2):
    p_1 = dict(p1)
    p_2 = dict(p2)

    maxx = max(len(p1),len(p2))
    max_dg = []
    for i in range(maxx):
        if len(p2)<len(p1):
            max_dg.append(p1[i][0])
        else:
            max_dg.append(p2[i][0])
    print(max_dg)
    max_dg = max(max_dg)
    out = dict()
    ou = []
    for i in range(max_dg+1):
        if i in p_1 and i not in p_2:
            out[i] = p_1[i]
            if out[i] != 0:
                
                ou.append((i,out[i]))
        elif i not in p_1 and i in p_2:
            out[i] = p_2[i]
            if out[i] != 0:
               
                ou.append((i,out[i]))
        elif i in p_1 and i in p_2:
            out[i] = p_1[i] + p_2[i]
            if out[i] != 0:
               
                ou.append((i,out[i]))

    ou.reverse()
    return ou


def main():
    p1 = [(4, 2), (0, 0),(1,1),(2,2)]
    p2 = [(4, -1), (0, 0)]
    print(polynomial_addition(p1, p2))

if __name__ == '__main__':
    main()

