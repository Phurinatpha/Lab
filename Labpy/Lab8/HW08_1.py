def main():
    print(moving_average([1, 2, 3, 4, 5],3))

def moving_average(list_a, w,ltout=[]):
    if w-1==len(list_a):
        return ltout
    else :
        ltout += [(sum(list_a[0:w])/w)]
        return moving_average(list_a[1:],w,ltout)

if __name__ == '__main__':
    main()