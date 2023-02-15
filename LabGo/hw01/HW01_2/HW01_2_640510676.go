// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// HW01_2
// 204203 Sec 001

package main

import (
	"math"
	"strings"
)

func additiveInverse(x string) (string, int64) {
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

	return string(result), twosComplToInt(string(result))
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
