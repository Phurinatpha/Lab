#!/usr/bin/env python3
# ภููริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab Quiz 3
# Problem 1
# 204111 Sec 002

from itertools import chain, combinations

def subset(set_a,n):
 	return [set(s) for s in power_set(set_a)]

def power_set(A):
    length = len(A)
    l = [a for a in A]
    ps = set()

    for i in range(2 ** length):
        selector = f'{i:0{length}b}'
        subset = {l[j] for j, bit in enumerate(selector) if bit == '1'}
        ps.add(frozenset(subset))
    
    return ps
	
def main():
	print(subset({'d', 's', 'c', 'x'},5))

if __name__ == '__main__':
	main()