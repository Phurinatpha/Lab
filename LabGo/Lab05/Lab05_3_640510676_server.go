// socket SERVER for golang
// https://golangr.com
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	fmt.Println("Start server...")
	// listen on port 8000
	ln, _ := net.Listen("tcp", ":8000")
	// accept connection
	for {
		conn, _ := ln.Accept()
		fmt.Println("Accepted connection.")
		go func() { // Do in another thread (Create new Goroutine)
			for {
				client_buffer := bufio.NewReader(conn)
				message, _ := client_buffer.ReadString('\n')
				
				fmt.Print("Message Received: ", string(message))
				// send to client
				keyboard_buffer := bufio.NewReader(os.Stdin)
				fmt.Print("Text to send: ")
				text, _ := keyboard_buffer.ReadString('\n')
				fmt.Fprintf(conn, text+"\n")
			}
		}()
	}
}
