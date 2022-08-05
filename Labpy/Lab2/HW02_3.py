x = float(input("Old price: "))

re = (98 - (x-50)%100) + (x-50)

print("New Price:",int(re))