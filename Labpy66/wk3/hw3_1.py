import math
def nearest_odd(x):
    return (2*(math.ceil(x/2)))-1

def main():
    test_nearest_odd()
    # x = float(input())
    # print(nearest_odd(x))

def test_nearest_odd():
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("ALL OK!")

if __name__ == '__main__':
    main()