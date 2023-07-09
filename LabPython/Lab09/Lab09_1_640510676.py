#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 1
# 204111 Sec 002

def main():
    m1 = [[7, -2, 23, 23, 21], [6, 14, -5, -4, -9], [-9, 45, 38, 43, 12], [17, 17, 34, 21, 1], [21, 20, 9, 46, 49]]

    m2 = [[4, 18, 33], [-6, 12, 48], [-3, 50, 40], [-3, 24, 3], [-3, 15, 11], [33, 12, 26]]
    print(matrix_mult(m1, m2))


def matrix_mult(m1, m2):
    if len(m1[0]) != len(m2): #ถ้าหลัก m1 != แถว m2 จะคูณกันไม่ได้
        return None
    else:
        res = [[0 for x in range(len(m2[0]))] for y in range(len(m1))] 
        #สร้าง list ขนาดตาม แถว m1* หลักm2
        for i in range(len(m1)):            
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
    return res



if __name__ == '__main__':
    main()
