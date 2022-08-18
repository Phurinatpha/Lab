def main():
    print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))

def median_of_median(list_a) -> float:
    n = len(list_a)//3
    if len(list_a) <= 2:
        return recurmid(list_a)
    elif n==1:
        if len(list_a) %3 ==0:
            mid = list_a[:]
        else:
            list_ex = list_a[2:]
            mid = list_a[0:2] + [sum(list_a[2:])/len(list_a[2:])]
        return recurmid(mid)
    else:
        mid1 = median_of_median(list_a[0:n])
        mid2 = median_of_median(list_a[n:(n*2)])
        mid3 = median_of_median(list_a[(n*2):])
        return recurmid([mid1] + [mid2] + [mid3])

def recurmid(list_a):
    if len(list_a) == 2:
        return sum(list_a)/2
    elif len(list_a) == 1:
        return list_a[0]
    else:
        list_a.remove(max(list_a))
        list_a.remove(min(list_a))
        return recurmid(list_a)
    
        

if __name__ == '__main__':
    main()