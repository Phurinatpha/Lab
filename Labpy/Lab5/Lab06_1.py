
def gcd(x,y):
    if y == 0:
        return abs(x)
    else:
        return gcd(y,x%y)
def main():
    x = int(input())
    y = int(input())

    print(gcd(x,y))


if __name__ == '__main__':
    main()

	



