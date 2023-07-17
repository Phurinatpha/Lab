def octagon_area(x):
    return (x*x)-2*((x/3)*(x/3))

def main():
    x = float(input())
    print(octagon_area(x))

if __name__ == '__main__':
    main()
