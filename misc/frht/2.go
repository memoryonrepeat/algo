package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(K int, A []int) int {
	counter := make(map[int]int)
	for _, num := range A {
		if _, ok := counter[num]; ok {
			counter[num]++
		} else {
			counter[num] = 1
		}
	}
	count := 0
	for key, _ := range counter {
		if _, ok := counter[K-key]; ok {
			count += counter[key] * counter[K-key]
		}
	}
	return count
}
