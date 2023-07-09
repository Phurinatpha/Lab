def main():
    num = int(input("num: "))
    pos = int(input("pos: "))
    result = rotate(num, pos)
    print(type(result))
    print(result) 

def rotate(num, pos):
    dg = len(str(num))
    for i in range(abs(pos)):
        if pos > 0:
            x = num%10
            y = num//10
            result = (x*10**(dg-1)) + y
            num = result
        else:
            result = num%10**(dg-1)*10 + (num//10**(dg-1))
            num = result
    return result
    

if __name__ == '__main__':
    main()
