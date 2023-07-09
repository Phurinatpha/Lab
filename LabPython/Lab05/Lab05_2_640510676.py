#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 05
# Problem 2
# 204111 Sec 002

def is_p_triple(x, y, z):
    summ = (x+y+z) #หาผลรวสมเพื่อนำไปหาค่า mid
    maxx = max(x,y,z) #หาค่า max เพื่อไปแทนสมการพีทาโกลัสจากการหาค่า max()
    midd = summ-max(x,y,z)-min(x,y,z) #หาค่า mid นำผลรวมมาลบค่า min max 
    minn = min(x,y,z) #หาค่า min เพื่อไปแทน a ในสมการจาก min()     
    if ((maxx**2) == (midd**2) + (minn**2)): #สมการพีทาโกลัส
        return True 
    else:
        return False
    
def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(is_p_triple(x, y, z))

if __name__ == '__main__':
    main()
