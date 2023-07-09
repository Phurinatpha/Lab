#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 12
# Problem 1
# 204111 Sec 002

def gcd(x,y):
	if x==0:
		return y
	else:
		return gcd(y%x,x)

def main():
	print(gcd(18 ,12))

if __name__ == '__main__':
	main()
