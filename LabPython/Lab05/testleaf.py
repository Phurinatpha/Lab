d = int(input())
m = int(input())
y = int(input())

from datetime import date 

date1 = date(y, 4, 13) 
date2 = date(y, m, d)
delta = date1 - date2

if (date2>date1):
	y=y+1

	if ((y%4==0 or y%400==0) or y%100!=0):
		d = d+1
		print(366+delta.days)
	else:
		print(365+delta.days)

elif (date1>=date2):
	print(delta.days)
else:
	pass





