// socket SERVER for golang
// https://golangr.com

package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	fmt.Println("Start server...")
	// listen on port 8000
	ln, _ := net.Listen("tcp", ":8000")
	// accept connection
	for {
		conn, _ := ln.Accept()
		fmt.Println("Accepted connection.")
		name_buffer := bufio.NewReader(conn)
		name, _ := name_buffer.ReadString('\n')
		name = string(name)
		name = strings.Replace(name, "\n", "", 1)

		/*
			blacklist := "first tawan wan sun tird"
			if strings.Index(blacklist, name) != -1 {
				println("Disconnect")
				break
			}
		*/

		go func() { // Do in another thread (Create new Goroutine)
			for {
				client_buffer := bufio.NewReader(conn)
				message, _ := client_buffer.ReadString('\n')

				fmt.Print(name+" said: ", string(message))
				// send to client
				keyboard_buffer := bufio.NewReader(os.Stdin)

				fmt.Printf("reply to %s: ", string(name))
				text, _ := keyboard_buffer.ReadString('\n')
				fmt.Fprintf(conn, text+"\n")
			}
		}()
	}
}
