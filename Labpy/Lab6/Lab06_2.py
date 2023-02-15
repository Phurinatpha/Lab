
def reverse_digits(x,s=1):
    if x != abs(x):
        s = -1
        x = abs(x)
    return s*rev(x)

def rev(x,su=0):
    if x>0:
        su = (su*10) + (x%10)
        return rev(x//10,su)
    else :
        return su

def main():
    x = int(input())
    print(reverse_digits(x))


if __name__ == '__main__':
    main()

	



