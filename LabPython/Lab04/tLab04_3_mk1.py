#!/usr/bin/env python3
# ชื่อ นามสกุล
# รหัสนักศึกษา
# Lab 04
# Problem 3
# 204111 Sec ???

def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
    p_pos = c//12 #ค่าที่เป็นไปได้

    if (p_pos >= p):
        xp = p*500
        
    #elif คอนดิที่ c evo ได้มากกว่า 2 เช่น 3 23
    elif (p_pos < p and p>=2):
        c = (c+p)-1
        p_pos1 = c//12
        xp = p_pos1*500

    elif (p>12 and c==0):   
        p = p-12
        c = (p+12)-1
        xp = 500

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
