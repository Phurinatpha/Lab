def main():

    n = 1
    nums = [1, 2, 3, 4]
    print(nums) #[1, 2, 3, 4]
    out = dest_rotate_list(nums, n)
    print(out)  #None
    print(nums) #[4, 1, 2, 3]

def dest_rotate_list(list_a, n):
    n = n%len(list_a)
    list_b = list_a[-n:] + list_a[:-n]
    list_a.extend(list_b)
    del list_a[:len(list_a)//2]
    
if __name__ == '__main__':
    main()