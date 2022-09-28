// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// Lab01_2
// 204203 Sec 001
package main

import (
	"math"
	"strconv"
	"strings"
)

const MAX_INT = 64
const DEC_PLACE = 6

func floatToBaseB(x float64, b uint8) string {
	sign := ""

	if x < 0 { // turn negative numbers to positive
		x = -x
		sign = "-"
	}

	// split at the decimal point
	front := int64(x)
	back := x - float64(front)
	//fmt.Print(back)
	frontStr := posIntToBaseB(front, b)
	backStr := fractionToBaseB(back, b)
	// putting every part together
	converted := sign + frontStr + "." + backStr

	return converted

}

func fractionToBaseB(x float64, b uint8) string {
	// only need to implement this function
	var result string
	var curr int

	for i := 0; i < 6; i++ {
		x *= float64(b)
		curr = int(math.Floor(x))

		if curr > 9 && b > 9 {
			switch curr {
			case 10:
				result += "A"
			case 11:
				result += "B"
			case 12:
				result += "C"
			case 13:
				result += "D"
			case 14:
				result += "E"
			case 15:
				result += "F"
			}
		} else {
			result += strconv.Itoa(curr)
		}
		x -= math.Floor(x)

	}

	return string(result)
}

func posIntToBaseB(x int64, b uint8) string {
	// this function is working correctly
	if x == 0 {
		return "0"
	}

	result := []byte(strings.Repeat("x", MAX_INT))
	k := MAX_INT - 1
	var currDigit byte

	for x > 0 {
		// calculate and convert back to char
		currDigit = byte((x % int64(b)) + int64('0'))
		if currDigit > '9' {
			currDigit = 'A' + currDigit - '9' - 1
		}
		result[k] = currDigit
		x = x / int64(b)
		k--
	}
	// convert from byte array to string
	return string(result[k+1:])
}
