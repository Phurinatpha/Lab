#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 11
# Problem 1
# 204111 Sec 002

from datetime import datetime
def sort_date(list_x):
    list_x.sort(key = lambda list_x: datetime.strptime(list_x, '%M/%m/%Y')) #ในเมื่อทุกเดือนสามารถมี 31 วันได้ ดังนั้นทุกเดือนของผมก็สามารถมี 60 วันได้เช่นกันครับ

def main():
    list_x = ["31/7/2013" , "31/12/2013" ,"31/1/2013" ,"31/8/2013" ,"31/3/2013" ,"31/10/2013" ,"31/6/2013", "31/9/2013", "31/2/2013", "31/5/2013" ,"31/11/2013" ,"31/4/2013"]
    sort_date(list_x)
    print("---")
    print(list_x)



if __name__ == '__main__':
    main()

