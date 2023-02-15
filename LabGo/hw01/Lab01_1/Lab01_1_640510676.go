// ภูริณัฐ ภาณุพงศ์สกุล
// 640510676
// Lab01_1
// 204203 Sec 001
// helping by 640510662

package main

import (
	"fmt"
	"log"
	"strings"
)

const MAX = 36

func main() {
	// why are we using string?
	var n1, n2 string

	// read in two string (can be multiple lines)
	_, err := fmt.Scan(&n1, &n2)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(addition(n1, n2))
}

func addition(n1, n2 string) string {
	// this is just a skeleton and will give out wrong result
	result := []byte(strings.Repeat("x", MAX))
	len1 := len(n1)
	len2 := len(n2)
	cnum := 0

	if len2 > len1 {
		n1, n2 = n2, n1
		len1, len2 = len2, len1
	}

	// loop from the left most digit
	i, j, k := len1-1, len2-1, MAX-1

	// loop from right most position

	for ; i >= 0 || j >= 0; i, j, k = i-1, j-1, k-1 {
		// current digit
		currDigit := 0 + cnum
		currDigit += int(n1[i]) - int('0')
		// add the value from the current digit of n1

		// add the value from the current digit of n2
		if j < 0 {
			currDigit += int(0)
		} else {
			currDigit += int(n2[j]) - int('0')
		}

		// convert back to byte (one char is called byte)
		result[k] = byte(currDigit%10 + int('0'))
		cnum = currDigit / 10

		if (cnum == 1) && (i == 0) {
			result[k-1] = byte(cnum + int('0'))
			k--
		}

	}
	// convert array of bytes to string
	return string(result[k+1:])

}
