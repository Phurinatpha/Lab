#!/usr/bin/env python3
# ภููริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab Quiz 3
# Problem 2
# 204111 Sec 002

def three_letters_count(text):
	let = text.lower().split()
	
	list_str = []
	for i in let:
		pos_st = 0
		len_pos = 3
		if len(i) > 3:
			while len(i) >= len_pos:
				list_str.append(i[pos_st:pos_st+3])
				pos_st += 1
				len_pos += 1
		else:
			list_str.append(i)
			pos_st += 1

	dic = {}
	for i in list_str:
		if i in dic:
			dic[i] += 1
		else:
			dic[i] = 1
	return dic

def main():
	print(three_letters_count("Wish you all good luck for the exam"))	#thx kub

if __name__ == '__main__':
	main()

"""
เว็ปช่วยชีวิต ใช้ dic[i] = list_st.count(i) แล้วแถกเลยไปหามาครับ แต่อย่าหาทำอีกนะครับสอบ quiz ก่อนสอบ final วันที่ 11 หวังว่าจะอ่านทันนะครับ
https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
"""
