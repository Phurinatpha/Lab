// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// HW01_3
// 204203 Sec 001

package main

import (
	"math"
	"strings"
)

func addNSubtract(n1, n2 string, bitLen uint8) (int64, int64) {
	len1 := len(n1)
	len2 := len(n2)

	if len2 > len1 {
		len1, len2 = len2, len1
		n1, n2 = n2, n1
	}

	if len1 != len2 {
		for i := (len1 - len2); i > 0; i-- {
			if n2[0] == '0' {
				n2 = string('0') + n2
			} else {
				n2 = string('1') + n2
			}
		}
	}

	len1, len2 = len(n1), len(n2)
	dif := math.Abs(float64(len1 - int(bitLen)))
	if dif != 0 {
		for i := dif; i > 0; i-- {
			if n1[0] == '1' {
				n1 = string('1') + n1
			} else {
				n1 = string('0') + n1
			}

			if n2[0] == '1' {
				n2 = string('1') + n2
			} else {
				n2 = string('0') + n2
			}
		}
	}
	return (add(n1, n2, bitLen)), add(n1, additiveInverse(n2), bitLen)
}

func add(n1, n2 string, bitLen uint8) int64 {
	result := []byte(strings.Repeat("x", int(bitLen)))
	len := len(n1) - 1
	k := int(bitLen) - 1
	car := 0

	for i := len; i >= 0; i-- {
		curr := 0 + car
		curr += int(n1[i]) - int('0')
		curr += int(n2[i]) - int('0')
		if curr == 2 {
			curr = 0
			car = 1
		} else if curr == 3 {
			curr = 1
			car = 1
		} else {
			car = 0
		}
		result[k] = byte(curr%10 + int('0'))
		if k == 0 {
			result[k] = byte(curr + int('0'))
			k--
			break
		}

		if (car == 1) && (i == 0) {
			result[k] = byte(car + int('0'))
			k--
		}
		k--
	}
	return twosComplToInt(string(result[:]))
}

func additiveInverse(x string) string {
	result := []byte(strings.Repeat("x", len(x)))
	for i := len(x) - 1; i >= 0; i-- {
		if x[i] == '1' {
			for j := i; j >= 0; j-- {
				if x[j] == '0' {
					result[j] = '1'
				} else {
					result[j] = '0'
				}
			}
			result[i] = '1'
			break
		} else {
			result[i] = x[i]
		}
	}
	return string(result)
}

func twosComplToInt(x string) int64 {
	var result int64 = 0
	var sign int = 1

	if x[0] == '1' {
		sign = -1
	}

	k := len(x) - 1
	for i := 0; i < len(x); i++ {
		if x[k] == '1' {
			if k == 0 && sign == -1 {
				result += -int64(math.Pow(2, float64(i)))
			} else {
				result += int64(math.Pow(2, float64(i)))
			}
		} else {
			result += 0
		}
		k--
	}
	return result
}