x = int(input())
y = int(input())
z = int(input())

summ = (x+y+z)
maxx = max(x,y,z)
midd = summ-max(x,y,z)-min(x,y,z)
minn = min(x,y,z)

print (maxx,midd,minn)