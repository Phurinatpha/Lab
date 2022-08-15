def main():
    print(moving_average([1, 2, 3, 4, 5],2))

def moving_average(list_a, w,ltout=[]):
    if w==len(list_a):
        return [(sum(list_a[0:w])/w)]
    elif w > len(list_a):
        return []
    else :
        return [(sum(list_a[0:w])/w)] + moving_average(list_a[1:],w,ltout)

if __name__ == '__main__':
    main()