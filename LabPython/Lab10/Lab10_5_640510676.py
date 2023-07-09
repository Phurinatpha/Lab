#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 5
# 204111 Sec 002

def decode(code_table, text):
    text = text.replace('\n',' \n ') #แทนที่ด้วยช่องว่างหน้าหลังจะได้ตัดออกมาได้
    text = text.split(' ')
    dec = ''
    for i in range(len(text)):
        if text[i].isnumeric(): #เช็คว่าเป็นตัวเลขไหม
            if int(text[i]) < len(code_table): #ไม่เกินขอบเขตทำอันนี้นะ
                dec += code_table[int(text[i])]
            else:   #เกินอันนี้นะ
                dec += "_"
        else:                   #อันนี้ไม่เป็นตัวเลขนะ
            if text[i] == "\n":     #ถ้าเป็น \n ก็ให้ขึ้นบรรทัดใหม่
                dec += "\n"         
            elif text[i] == '':     #ถ้าเป็น strว่าง ก็ช่างแม่มไม่ต้องทำไร
                pass
            else:                   #ถ้าเป็นเคสอื่นรวมถึงเคสลบด้วย
                dec += "_"
    print(dec)

def main():
    decode("aceiklmr-",'''
3
5 3 4 2
3 1 2 8 1 7 2 0 86
''')


if __name__ == '__main__':
    main()

