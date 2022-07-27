// ภูริณัฐ ภาณุพงศ์สกุล ล๊อคเก็ต
// 640510676
// HW02_2
// 204203 Sec 001

package main

import (
	"math"
	"strconv"
	"strings"
)

func roundToEven(x string, bPlace uint8) string {
	xsp := strings.Split(x, ".")
	decx := strings.Index(x, ".")
	var bk string
	fr := xsp[0]

	if decx > -1 {
		bk = xsp[1]
	} else {
		xsp[0] = x
	}

	if len(bk) < int(bPlace) {
		for i := (int(bPlace) - len(bk)); i > 0; i-- {
			bk += "0"
		}
		return fr + "." + bk
	}

	if int(bPlace) == len(bk) || (bPlace == 0) && (len(bk) == 0) {
		return x
	}

	if len(bk) > int(bPlace) {
		if len(bk) == 1 {
			fbk := bk[:int(bPlace)+1]

			if (fr[len(fr)-1] == '0') && (fbk == "1" || fbk == "0") {
				return fr
			}

			if (fr[len(fr)-1] == '1') && (fbk == "1") {
				return addition(fr, string(fbk), len(fr))
			} else if (fr[len(fr)-1] == '1') && (fbk == "0") {
				return fr
			}

		} else if len(bk) > 1 {
			if int(bPlace) == 0 {
				affbk := bk[int(bPlace):]
				if fr[len(fr)-1] == '0' {
					if check_half(affbk) {
						return addition(fr, "1", len(fr))
					} else {
						return fr
					}
				} else {
					if bk[0] == '1' {
						return addition(fr, "1", len(fr))
					} else {
						return fr
					}
				}
			}

			cbk := bk[:int(bPlace)]
			afcbk := bk[int(bPlace):]
			lastbk := cbk[int(bPlace)-1]

			if lastbk == '0' {
				if check_half(afcbk) {
					return fr + "." + addition(string(cbk), "1", len(cbk))
				} else {
					return fr + "." + cbk
				}
			} else if lastbk == '1' {
				if afcbk[0] == '1' {
					rou := addition(cbk, "1", len(cbk))
					if len(rou) > len(cbk) {
						addcarr := addition(fr, string(rou[0]), len(fr))
						return addcarr + "." + rou[1:]
					} else {
						return fr + "." + rou
					}
				} else {
					return fr + "." + cbk
				}
			}
		}
	}

	return ""
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

func check_half(str string) bool {
	var curr float64
	pow := -1
	for i := 0; i < len(str); i++ {
		num, _ := strconv.Atoi(string(str[i]))
		curr += float64(num) * math.Pow(2, float64(pow))
		pow--
	}

	if curr > 0.5 {
		return true
	}
	return false
}
