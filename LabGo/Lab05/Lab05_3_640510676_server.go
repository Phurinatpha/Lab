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

func check(err error, message string) {
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", message)
}

func main() {
	fmt.Println("Start server...")
	// listen on port 8000
	ln, err := net.Listen("tcp", ":8000")
	check(err, "Server is ready.")
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
