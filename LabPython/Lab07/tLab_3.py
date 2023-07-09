n = int(input('Enter number of rows required: '))

for i in range(n):
    for j in range(n-i):
        print('', end='') # printing space required and staying in same line
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print('*',end='')
        else:
            print('.', end='')
    print() # printing new line
