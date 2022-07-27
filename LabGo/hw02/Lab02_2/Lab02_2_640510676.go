// ภูริณัฐ ภาณุพงศ์สกุล ล๊อคเก็ต
// 640510676
// Lab02_2
// 204203 Sec 001

package main

import (
	"math"
	"strings"
)

const MAX = 141 // really?

func baseNAddition(r1, r2 string, base int) string {
	var fr1, fr2, bk1, bk2 string
	var r1sp, r2sp []string
	max := int(math.Max(float64(len(r1)), float64(len(r2))))
	dec1 := strings.Index(r1, ".")
	dec2 := strings.Index(r2, ".")

	if dec1 != -1 {
		r1sp = strings.Split(r1, ".")
	}
	if dec2 != -2 {
		r2sp = strings.Split(r2, ".")
	}

	if dec1 != -1 && dec2 != -1 {
		fr1 = r1sp[0]
		bk1 = r1sp[1]
		fr2 = r2sp[0]
		bk2 = r2sp[1]
	} else if dec1 != -1 && dec2 == -1 {
		fr1 = r1sp[0]
		bk1 = r1sp[1]
		fr2 = r2
		bk2 = ""
	} else if dec1 == -1 && dec2 != -1 {
		fr1 = r1
		bk1 = ""
		fr2 = r2sp[0]
		bk2 = r2sp[1]
	} else {
		fr1 = r1
		fr2 = r2
		bk1 = ""
		bk2 = ""
	}

	if len(fr1) != len(fr2) {
		for i := 0; i < max; i++ {
			if len(fr1) < len(fr2) {
				fr1 = "0" + fr1
			} else if len(fr2) < len(fr1) {
				fr2 = "0" + fr2
			}
		}
	}

	if len(bk1) != len(bk2) {
		for i := 0; i < max; i++ {
			if len(bk1) < len(bk2) {
				bk1 += "0"
			} else if len(bk2) < len(bk1) {
				bk2 += "0"
			}
		}
	}

	if dec1 != -1 || dec2 != -1 {
		r1 = fr1 + "." + bk1
		r2 = fr2 + "." + bk2
	} else {
		r1 = fr1
		r2 = fr2
	}

	return addition(r1, r2, base)
}

func addition(n1, n2 string, base int) string {

	result := []byte(strings.Repeat("x", MAX))
	len1 := len(n1)
	len2 := len(n2)
	carry := 0

	i, j, k := len1-1, len2-1, MAX-1

	for ; i >= 0 || j >= 0; i, j, k = i-1, j-1, k-1 {
		temp := carry
		carry = 0
		if string(n1[i]) != "." { // j>i ทำให้ i-1
			if i >= 0 {
				temp += int(n1[i]) - int('0')
			}
			if j >= 0 {
				temp += int(n2[j]) - int('0')
			}
			result[k] = byte((temp % base) + int('0'))
			carry = temp / base
		} else {
			result[k] = byte('.')
			if temp > 0 {
				carry = 1
			}
		}
	}

	if carry > 0 {
		result[k] = '1'
	} else {
		k++
	}

	return string(result[k:])
}
