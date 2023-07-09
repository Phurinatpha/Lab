#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 2
# 204111 Sec 002
def main():
    list_a = [[-90, 792211125, 193211887, 512625, 15946], 
            [2456154, 784544, 3409, -34, 34435650], 
            [86344748, 8595, 10731, 68917423, 790], 
            [-44, 83359668, 5450, 72041837, 8910], 
            [-31, 4732265, 1305918, 86762, 738], 
            [167, 1280174, 9582002, 1613742, 4951079], 
            [807920877, 85, 62, -33, 523030], 
            [2327326, 1699, 477, 12407812, -65], 
            [-26, 34777730, -50, 56968277, 63821884], 
            [114626216, 288719710, -84, 301259, 916114],
            [52054, 6593, 47865, 6166, -78]]

    row = -13
    col = 1

    print(remove_row_col(list_a, row, col))

def remove_row_col(list_a, row, col):
    if row == -1: #กรณีที่ row เป็นลบ 1 จะ slicing แค่ตัวเริ่มต้น
        list_b = list_a[:row]
    elif (row != -1): #จะ slicing ตัวหน้า + หลัง
        list_b = list_a[:row] + list_a[row+1:]
    list_b = list(map(list , zip(*list_b))) #ทำการ map(zip)เปลี่ยนหลักเป็นแถวเพื่อตัดใน col

    if col == -1: #กรณีที่ row เป็นลบ 1 จะ slicing แค่ตัวเริ่มต้น
        list_c = list_b[:col] 
    else:       
        list_c = list_b[:col] + list_b[col+1:]#จะ slicing ตัวหน้า + หลัง
    list_c = list(map(list, zip(*list_c))) #map zip คืนให้เป็นแบบที่ต้องการ
    
    return list_c



if __name__ == '__main__':
    main()
