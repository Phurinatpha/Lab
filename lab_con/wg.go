package main
import (
    "fmt"
    "sync"
)

var mu sync.Mutex
var wg sync.WaitGroup
var sum = 0

func counter(n int, wg *sync.WaitGroup){
    for i := 0; i < 10000; i++ {
        add(1)
    }
    fmt.Println("From ", n, ":", sum) 
    wg.Done()
}

func add(a int) {
    mu.Lock()
    sum = sum + a
    mu.Unlock()
}

func main() {
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go counter(i, &wg)
    }

    wg.Wait()
    fmt.Println("Final Sum:", sum)
}