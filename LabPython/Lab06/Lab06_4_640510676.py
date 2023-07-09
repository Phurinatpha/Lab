#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 06
# Problem 4
# 204111 Sec 002

def main():
    # ด้านล่างเป็นแค่โครงสำหรับการแสดงผล นักศึกษาสามารถเขียนเพิ่มหรือแก้ไขตามความเหมาะสม
    total = int(input("Total students: ")) #Input amout student
    print('Enter score:')
    score = 0
    maxx = 0
    totalsc = 0
    runup = 0
    for i in range(total):
        score = int(input()) #รับค่า score 
        totalsc = totalsc + score #ผลรวมของ score
        av = totalsc/total #av ที่ได้จากการนำ score มาหารด้วย total
        if (score > maxx):  #ถ้าค่า score มากกว่า max เดิม
            runup = maxx    #ค่ารองจะมีค่า = ค่า max เดิม
            maxx = score    #score = maxใหม่
        else: pass
        if (score > runup and score < maxx): #กรณีในกรณีที่ค่า score มีค่ามากกว่าค่า run และ score<max ให้ runup=score 
           runup = score
        else: pass

    print('---')
    print('Max score is: %.2f' %maxx)
    if (runup == 0):
        print('Runner up is: None')
    else:
        print('Runner up is: %.2f' %runup)
    print('Average is: %.2f' %av)

if __name__ == '__main__':
    main()
