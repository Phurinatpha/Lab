m1 =float(input("m1: ")) 
b1 =float(input("b1: "))

m2 =float(input("m2: ")) 
b2 =float(input("b2: ")) 

x = -((b1-b2)/(m1-m2)) 
y = (m1*x)+b1
print ("Lines intersect at (%.2f,%.2f)" %(x,y))