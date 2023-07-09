#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 3
# 204111 Sec 002

def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
    p_pos = c//12 #ค่าที่เป็นไปได้นการ evo 

    if (p_pos >= p): #ค่าที่สามารถ evo ได้มีมากกว่าหรือเท่ากับ p ที่มีอยู่ xp ที่ได้จะเท่ากับ จำนวน p ที่มีอยู่คูณด้วยค่าที่มาจาก evo แต่ละขึ้น (500)
        xp = p*500

    #elif ที่ c evo ได้มากกว่า 2 เช่น 3 23
    elif (p_pos < p and p>=2): #
        c = (c+p)-1
        p_pos1 = c//12
        xp = p_pos1*500

    elif (p_pos < p and p>=1):
        c = (c+p)-1
        p_pos1 = c//12
        xp = p_pos1*500

    else:
        xp = 0

    return xp

def main():
    # receive input from user
    p = int(input())
    c = int(input())
    # print result from function
    print(calculate_p2p_evolve_exp(p, c))

if __name__ == '__main__':
    main()