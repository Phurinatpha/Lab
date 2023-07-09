#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 5
# 204111 Sec 002

def main():
    p = [(0,0), (0,1), (0, -1), (0, 0.5), (0, -0.5), (1, 0), (1, 1), (1, -1), (1, 0.5), (1, -0.5)]
    x = 'x'
    print(print_polynomial(p, x))

def print_polynomial(p, x):
    p = list(reversed(sorted(p)))

    for i in p:
        for j in p:
            if j[1] == 0:
                p.remove(j)
    out = []
    first = True
    for i in p:
        cof = i[1]
        if first:
            if cof > 0:
                si = ""
            else:
                si = '-'
            first = False
        else:
            if cof > 0:
                si = " + "
            else:
                si = " - "


        if abs(i[1]) == 1:                                      #สัมประสิทธิเป็น 1 
            if i[0] == 1:                                       # ยกกำลังเป็น 1  สัมประสิทธิเป็น 1 
                sr = '{2}{3}'.format(abs(cof),i[0],si,x)        
            elif i[0] == 0:                                     # ยกกำลังเป็น 0  สัมประสิทธิเป็น 1
                sr = '{2}{0}'.format(abs(cof),i[0],si,x)
            else:                                               # ยกกำลังมากกว่า 1 แต่ สัมประสิทธิ 1 
                sr = '{2}{3}^{1}'.format(abs(cof),i[0],si,x)
        elif i[0] > 1:                                          # ยกกำลังมากกว่า 1 สัมประสิทธิมากกว่า 1 
            sr = '{2}{0}{3}^{1}'.format(abs(cof),i[0],si,x)     
        elif i[0] == 1:                                         # ยกกำลังเป็น 1 
            sr = '{2}{0}{3}'.format(abs(cof),i[0],si,x) 
        elif i[1] == 0:                                         # สัมประสิทธิเป็น 0
            pass
        else:
            sr = '{2}{0}'.format(abs(cof),i[0],si,x)
        out.append(sr)
       
    return "".join(out)

if __name__ == '__main__':
    main()

