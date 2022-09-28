
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(abs(y),abs(x)%y)
def main():
    x = int(input())
    y = int(input())

    print(gcd(x,y))


if __name__ == '__main__':
    main()

	



