#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 04
# Problem 3
# 204111 Sec 002

def calculate_p2p_evolve_exp(p, c):
    # WRITE YOUR CODE HERE
     #ค่าที่เป็นไปได้ในการ evo 
    p_pos = (p+c//11)
    if p/c<=(1/11)and p>0: #ค่าที่สามารถ evo ได้มีมากกว่าหรือเท่ากับ p ที่มีอยู่ xp ที่ได้จะเท่ากับ จำนวน p ที่มีอยู่คูณด้วยค่าที่มาจาก evo แต่ละขั้น(500)
        xp = p*500

    #elif ที่ c evo ได้มากกว่า 1 เช่น 3 23
    elif (p > p_pos and p>=1) : #ให้ p มากกว่าค่าที่เป็นไปได้ในการ evo(p_pos) และ p มีขั้นต่ำที่ 1 ตัว
        p_pos1 = ((c+p)-2)//11 #หาจำนวนการ evo ที่ได้จากกรณีนกมากกว่า 1 ตัวและมีแคนดีมากพอในการ evo
        xp = p_pos1*500

    else: #นอกจากกรณีที่กล่าวมาให้ xp=0
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