def main():
    side = float(input("side length: "))
    run = octagon_area(side)
    print("%.2f" %run)

def octagon_area(x):
    square_area = x*x
    triangle_area = (0.5)*(x/3)*(x/3)
    octagonal_area = (square_area)-(triangle_area)**4

    return octagonal_area

if __name__ == '__main__':
    main()