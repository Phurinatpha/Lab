// ชิกานดา ณ มณี_มะงิ้ง
// 640510610
// HW02_2
// 204203 Sec 001

package main

import (
	"math"
	"strconv"
	"strings"
)

func roundToEven(x string, bPlace uint8) string {
	st := strings.Split(x, ".")
	st0 := st[0]
	var st1, str, res string

	if strings.Index(x, ".") > -1 {
		st1 = st[1]
	}

	if int(bPlace) == len(st1) {
		res = x
		return res
	}

	if len(st1) < int(bPlace) {
		str = strings.Repeat("0", int(bPlace)-len(st1))
		st1 += str
		res = st0 + "." + st1
		return res
	}

	if len(st1) > int(bPlace) {
		if len(st1) == 1 {
			cutst := st1[:int(bPlace)+1]
			if (st0[len(st0)-1] == '1') && (cutst == "1") {
				roundCut := addition(st0, string(cutst), len(st0))
				res = roundCut
				return res
			} else if (st0[len(st0)-1] == '1') && (cutst == "0") {
				res = st0
				return res
			}

			if (st0[len(st0)-1] == '0') && (cutst == "1" || cutst == "0") {
				res = st0
				return res
			}

		} else if len(st1) > 1 {

			if int(bPlace) == 0 {
				cutzero := st1[int(bPlace):]
				if st0[len(st0)-1] == '0' {
					if checkCountOne(cutzero) {
						st0 = addition(st0, "1", len(st0))
						res = st0
						return st0
					} else {
						return st0
					}
				} else {
					if st1[0] == '1' {
						st0 = addition(st0, "1", len(st0))
						return st0
					} else {
						return st0
					}
				}
			}

			cutst1 := st1[:int(bPlace)]
			backcut := st1[int(bPlace):]
			l_word := cutst1[int(bPlace)-1]

			if l_word == '0' {
				if checkCountOne(backcut) {
					rounded := addition(string(cutst1), "1", len(cutst1))

					res = st0 + "." + rounded
					return res
				} else {
					res = st0 + "." + cutst1
					return res
				}

			} else if l_word == '1' {

				if backcut[0] == '1' {
					rounded := addition(string(cutst1), "1", len(cutst1))
					if len(rounded) > len(cutst1) {
						overLen := string(rounded[0])
						add2Int := addition(st0, string(overLen), len(st0))
						rounded = rounded[1:]

						res = add2Int + "." + rounded
						return res

					} else {
						res = st0 + "." + rounded
						return res
					}
				} else {
					res = st0 + "." + cutst1
					return res
				}
			}
		}
	}

	return res
}

func checkCountOne(backb string) bool {
	lenc := len(backb)
	var curr float64
	power := -1
	for i := 0; i < lenc; i++ {
		num, _ := strconv.Atoi(string(backb[i]))
		curr += float64(num) * math.Pow(2, float64(power))
		power--
	}

	if curr > 0.5 {
		return true
	}
	return false

}

func addition(n1, n2 string, bPlace int) string {
	result := []byte(strings.Repeat("x", bPlace+1))
	len1 := len(n1)
	len2 := len(n2)
	if len1 > len2 {
		for l := len1 - 1; l > 0; l-- {
			n2 = "0" + n2
		}
	}
	len2 = len(n2)

	carry := 0
	i, j, k := len1-1, len2-1, bPlace
	for ; i >= 0 || j >= 0; i, j, k = i-1, j-1, k-1 {
		temp := carry
		carry = 0
		if i >= 0 {
			temp += int(n1[i]) - int('0')
		}

		if j >= 0 {
			temp += int(n2[j]) - int('0')
		}

		result[k] = byte((temp % 2) + int('0'))

		carry = temp / 2
	}

	if carry > 0 {
		result[k] = '1'
	} else {
		k++
	}
	return string(result[k:])
}
