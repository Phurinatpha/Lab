# ภูริณัฐ  ภาณุพงศ์สกุล
# 640510676
# Lab 03
# Problem 2
# 204111 Sec 002

def reverse_digits(x): #เป็นการจัดลำดับโดยใช้แนวคิดทางคณิตศาสตร์
    # เขียนโค้ดเพิ่มตรงนี้
    r0 = x%10                #นำหลักหน่วย % ด้วยค่าหลักสิบเพื่อให้สลับไปเป็นค่าแรก
    r1 = (x//10)%10          #นำหลักสิบ // ด้วย 10(10**1) เพื่อตัดเศษในหลักหน่วยออกแล้ว % ด้วย 10 เพื่อให้ได้ค่าในหลักสิบ
    r2 = (x//100)%10         #นำหลักร้อย // ด้วย 100(เป็นค่าประจำหลักจาก 10**2 หลักร้อย) เพื่อตัดเศษแล้ว % 10 เพื่อเอาเศษไปเป็นค่าหลักร้อย  
    r3 = (x//1000)%10        #นำหลักพัน // ด้วย 1000(10**3) แล้ว % 10 
    Rall = int('{0}{1}{2}{3}'.format(r0,r1,r2,r3))  #นำเอาค่า r0 r1 r2 r3 มาจัดให้ได้ไในแบบที่ต้องการ
    return Rall #ส่งค่ารีอออกมา

def main():
    # รับตัวเลขจาก user
    x = int(input())
    # พิมพ์ตัวเลขกลับด้าน
    print(reverse_digits(x)) #เรียกผลจาก func. มาแสดงผล

if __name__ == '__main__':
    main()

