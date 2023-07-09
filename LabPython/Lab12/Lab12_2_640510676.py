#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 12
# Problem 2
# 204111 Sec 002

def n_base_to_10(n, num):
	if num == 0:
		return num
	x= n*(n_base_to_10(n ,num//10))
	y=(num%10)
	return  x+y

def main():
	print(n_base_to_10(2, 10110))

if __name__ == '__main__':
	main()
