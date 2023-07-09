number = int(input('Input number: '))
k = int(input('Input digit: '))
value = int(input('Input digit: '))

kth1 = (((abs(number)//(10**k))*10**k))+(value*10**k)
Number = number-kth1



print (kth1)
print (Number)


