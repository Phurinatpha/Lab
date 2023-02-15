import math

x =  int(input("Input milliseconds: "))
day1 =(x//86400000)
hr1 =((x%86400000)//3600000)
min1 =(((x%86400000)%3600000)//60000)
s =((((x%86400000)%3600000)%60000)//1000)
ms =(x%1000)
print("%.d day(s), %.d hour(s), %.d minute(s), %.d second(s), and %.d millisec(s)" %(day1,hr1,min1,s,ms))