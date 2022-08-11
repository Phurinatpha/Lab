


def main():
    print(is_anagram('I am Lord Voldemort!!! ', 'Tom Marvolo Riddle'))

def is_anagram(str1,str2):
    lens1 = len(str1)
    str1 = (sorted(str1,lens1))
    str1 = quicksort(str1)

    lens2 = len(str2)
    str2 = (sorted(str2,lens2))
    str2 = quicksort(str2)

    #print(str1)
    #print(str2)
    if str1 == str2 and len(str1) == len(str2):     #ถ้าlist เท่ากัน ขนาดต้องเท่ากันและทุกตัวเท่ากัน
        return True                     
    else:                               #ถ้าไม่ก็ส่ง false
        return False

def sorted(str1,lens,i=0,str = ""):
    if lens == 0 :
        return str
    else:
        if str1[i].isalpha():
            str = (''.join([str,str1[i]])).casefold()
            
    return sorted(str1,lens-1,i+1,str)

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

if __name__ == '__main__':
    main()
