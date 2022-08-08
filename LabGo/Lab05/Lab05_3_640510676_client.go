// socket client for golang
// https://golangr.com
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// connect to server
	conn, _ := net.Dial("tcp", "127.0.0.1:8000")
	fmt.Print("Input your name: ")
	name_buffer := bufio.NewReader(os.Stdin)
	name, _ := name_buffer.ReadString('\n')

	fmt.Print("Welcome " + name)
	fmt.Fprintf(conn, name+"\n")
	for {
		// create buffer to get keyboard input
		keyboard_buffer := bufio.NewReader(os.Stdin)
		fmt.Print("Text to send: ")
		text, _ := keyboard_buffer.ReadString('\n')
		// send to server

		fmt.Fprintf(conn, text+"\n")
		// create buffer and recieve from conn
		server_buffer := bufio.NewReader(conn)
		message, _ := server_buffer.ReadString('\n')
		fmt.Print("Message from server: " + message)
	}
}
