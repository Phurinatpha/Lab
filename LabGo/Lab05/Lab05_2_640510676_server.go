// socket SERVER for golang
// https://golangr.com
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
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
