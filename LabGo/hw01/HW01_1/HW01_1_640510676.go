// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// HW01_1
// 204203 Sec 001

package main

import (
	"math"
)

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
