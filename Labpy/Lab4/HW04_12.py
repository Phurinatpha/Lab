#!/usr/bin/env python

def main():
    p = int(input("p: "))
    c = int(input("c: "))
    print(calculate_p2p_evolve_exp(p, c))


def calculate_p2p_evolve_exp(p, c):
    if p==0:
    	return 0
    elif (c - (p*12)+(p-1)) >=p:
        return p*500
    return ((p+c-2)//11)*500

   
   
    
if __name__ == '__main__':
    main()
    