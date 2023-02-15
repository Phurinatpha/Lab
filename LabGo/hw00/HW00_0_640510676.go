// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// HW00_0
// Problem A
// 204203 Sec 001

package main

func factorial(num1 int8) int64 {
	var result int64 = 1
	for i := 0; i < int(num1); i++ {
		result *= int64(num1) - int64(i)
	}

	return result
}
