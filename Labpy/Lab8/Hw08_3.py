
def main():
    print(medal_allocation([9,9,0,0,0,0]))

def medal_allocation(list_a):
    list_a = sorted(list_a,reverse=True)
    if 0 in list_a:
        list_a = list_a = list_a[:list_a.index(0)]

    gold = list_a[:list_a.count(max(list_a))]
    list_a = list_a[list_a.count(max(list_a)):]
    if len(list_a) == 0:
        return gold,[],[]
    elif len(list_a) != 0:
        sil = list_a[:list_a.count(max(list_a))]
        list_a = list_a[list_a.count(max(list_a)):]

    if len(list_a) != 0:
        bronze = list_a[:list_a.count(max(list_a))]
    else:
        bronze = []


    if len(gold) == 1 and len(sil)==1:
        return gold,sil,bronze
    elif len(gold) == 2:
        return gold,[],sil
    elif len(gold) == 1 and len(sil)>=2:
        return gold,sil,[]
    else:
        return gold,[],[]


        

if __name__ == '__main__':
    main()