def main():
    print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))

def median_of_median(list_a) :
    list_a = list(map(float,list_a))
    if len(list_a) == 1:
        return list_a[0]
    elif len(list_a) == 2:
        return sum(list_a)/2
    elif len(list_a) == 3:
        list_a.remove(max(list_a))
        list_a.remove(min(list_a))
        return list_a[0]
    else:
        n = len(list_a)//3
        mid1 = median_of_median(list_a[0:n])
        mid2 = median_of_median(list_a[n:(n*2)])
        mid3 = median_of_median(list_a[(n*2):])
        return median_of_median([mid1,mid2,mid3])

if __name__ == '__main__':
    main()