// ภูริณัฐ ภาณุพงศ์สกุล ล๊อคเก็ต
// 640510676
// HW02_1
// 204203 Sec 001

package main

import (
	"strconv"
	"strings"
)

func ipv4Encode(ipString string) uint32 {
	//var result uint32 = 0
	var enc [4]int
	numSet := strings.Split(ipString, ".")

	enc[0], _ = (strconv.Atoi(string(numSet[0])))
	enc[1], _ = (strconv.Atoi(string(numSet[1])))
	enc[2], _ = (strconv.Atoi(string(numSet[2])))
	enc[3], _ = (strconv.Atoi(string(numSet[3])))

	return uint32(enc[0]<<24 | enc[1]<<16 | enc[2]<<8 | enc[3])
}

func ipv4Decode(ipUint uint32) string {
	var dec [4]string

	dec[0] = strconv.Itoa(int(ipUint) & 0xff)
	dec[1] = strconv.Itoa(int(ipUint>>8) & 0xff)
	dec[2] = strconv.Itoa(int(ipUint>>16) & 0xff)
	dec[3] = strconv.Itoa(int(ipUint>>24) & 0xff)
	return dec[3] + "." + dec[2] + "." + dec[1] + "." + dec[0]
}
