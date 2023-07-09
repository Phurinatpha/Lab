#!/usr/bin/env python3
# ภููริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab Quiz 3
# Problem 1
# 204111 Sec 002

from itertools import chain, combinations
def subset(set_a,n):
    s = list(set_a)
    sub = list(chain.from_iterable(combinations(s, r) for r in range(n+1)))
    return sorted(list(map(set,sub)))


def main():
	print(subset({'d', 's', 'c', 'x'},5))

if __name__ == '__main__':
	main()