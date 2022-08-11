
def main():
    print(is_anagram('I am Lord Voldemort', 'Tom Marvolo Riddle'))

def is_anagram(str1,str2,i=0):
    s1 = str1.replace(" ","").lower()
    s2 = str2.replace(" ","").lower()

    if len(s1) == i:
        return True
    elif len(s1) == len(s2):
        if s1.count(s1[i]) == s2.count(s1[i]):
            return is_anagram(s1,s2,i+1)
    return False

if __name__ == '__main__':
    main()
