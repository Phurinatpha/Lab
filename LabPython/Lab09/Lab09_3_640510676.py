#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 3
# 204111 Sec 002

def main():
    board = [[8, 1, 6],
            [3, 5, 7],
            [2, 9, 4]]

    print(is_magic_square(board))

def is_magic_square(board):
    n = len(board)
    sumd1=0
    sumd2=0
    #เช็คเส้นทะแยง
    for i in range(n):
        sumd1 += board[i][i]
        sumd2 += board[i][n-i-1] 
    if not(sumd1 == sumd2):
        return False

    #เช็คแถวว่า + ได้เท่ากันหรือไม่
    for i in range(n):
        s_row = 0
        s_col = 0
        for j in range(n):
            s_row += board[i][j]
            s_col += board[j][i]
        if not(s_row == s_col == sumd1):
          return False
    if board[0].count(board[0][0]) >= 2:
        return False
    
    #เช็คกรณีค่าเกินขอบเขตของ n*n  
    map_z = []        
    for i in range(n):
        map_z.extend(board[i])
    for i in map_z:
        if i > n**2:
            return False
    return True



if __name__ == '__main__':
    main()

