x =  int(input("Input milliseconds: "))

day1 =(x//86400000) 
day2 =(x%86400000)

hr1 =(day2//3600000)
hr2 =(day2%3600000)

min1 =(hr2//60000)
min2 =(hr2%60000)

s =(min2//1000)

ms =(x%1000)

print("%.d day(s), %.d hour(s), %.d minute(s), %.d second(s), and %.d millisec(s)" %(day1,hr1,min1,s,ms))